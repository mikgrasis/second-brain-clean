#!/usr/bin/env python3
"""Number [@key] citations and write each note's ## References block from a BibTeX file.

Usage: python3 _scripts/build_references.py [--check] [--bib library.bib] [--library VAULT] [--csl _scripts/ieee.csl] [folder ...]

Defaults: library.bib at the vault root, _scripts/ieee.csl, folders atoms/ and molecules/. Needs pandoc.

With --library, the bibliography is that library vault's library.bib (unless --bib says otherwise), and
each entry links to the paper's note there, references/<key>.md, when it exists.

In a note, write [@key], [@a; @b, p. 3] or @key. The script numbers them by first appearance,
[@a; @b, p. 3] -> \\[[[#^ref-a|1]], [[#^ref-b|2]], p. 3\\], and writes the entries, formatted by pandoc
citeproc, under ## References between %% refs:start %% and %% refs:end %%. Every run turns the numbers
back into keys first, so edit with keys or numbers alike and rerun. --check changes nothing and exits 1
if a note would change. Keys missing from the bibliography are left as written and reported.
"""
import argparse, pathlib, re, subprocess, sys
from urllib.parse import quote

VAULT = pathlib.Path(__file__).resolve().parent.parent
KEY = r"[A-Za-z0-9_][A-Za-z0-9_:.\-]*[A-Za-z0-9_]"
GROUP = re.compile(r"\[([^\[\]\n]*?@" + KEY + r"[^\[\]\n]*)\]")
BARE = re.compile(r"(?<![\w@\[`])@(" + KEY + r")")
NUM_GROUP = re.compile(r"\\\[([^\n]*?\[\[#\^ref-[^\n]*?)\\\]")
NUM_ITEM = re.compile(r"\[\[#\^ref-([A-Za-z0-9-]+)\\?\|\d+\]\]")
REFS = re.compile(r"\n*## References\n\n%% refs:start[^\n]*%%\n.*?%% refs:end %%\n?", re.S)
CODE = re.compile(r"^```.*?^```|`[^`\n]*`", re.S | re.M)


def block_id(key):
    return "ref-" + re.sub(r"[^A-Za-z0-9-]", "-", key)


def masked(text, fn):
    """Apply fn to text with code spans and fences held out."""
    held = []
    out = fn(CODE.sub(lambda m: held.append(m.group(0)) or f"\x00{len(held) - 1}\x00", text))
    text, rest = (out[0], out[1:]) if isinstance(out, tuple) else (out, ())
    text = re.sub(r"\x00(\d+)\x00", lambda m: held[int(m.group(1))], text)
    return (text, *rest) if rest else text


def unnumber(text, ids):
    def group(m):
        inner = NUM_ITEM.sub(lambda i: "@" + ids.get(i.group(1), i.group(1)), m.group(1))
        return "[" + re.sub(r", (?=@)", "; ", inner) + "]"
    return NUM_GROUP.sub(group, text)


def number(text, keys):
    order = []
    for m in re.finditer(r"@(" + KEY + r")", text):
        if m.group(1) in keys and m.group(1) not in order:
            order.append(m.group(1))
    num = {k: i + 1 for i, k in enumerate(order)}
    link = lambda k: f"[[#^{block_id(k)}|{num[k]}]]"

    def group(m):
        out = []
        for part in [p.strip() for p in m.group(1).split(";")]:
            pm = re.match(r"^(.*?)@(" + KEY + r")\s*,?\s*(.*)$", part)
            if not pm or pm.group(2) not in num:
                return m.group(0)
            pre, k, loc = pm.groups()
            out.append((pre + " " if pre.strip() else "") + link(k) + (", " + loc if loc else ""))
        return "\\[" + ", ".join(out) + "\\]"
    text = GROUP.sub(group, text)
    text = BARE.sub(lambda m: "\\[" + link(m.group(1)) + "\\]" if m.group(1) in num else m.group(0), text)
    # inside a table row the link's pipe must be escaped, or it splits the cell
    text = re.sub(r"(?m)^\|.*$", lambda m: re.sub(r"(\[\[#\^ref-[A-Za-z0-9-]+)\|(\d+\]\])", r"\1\\|\2", m.group(0)), text)
    return text, order


def render(keys, bib, csl):
    doc = " ".join(f"[@{k}]" for k in keys) + "\n"
    cmd = ["pandoc", "-f", "markdown", "-t", "commonmark-raw_html", "--wrap=none", "--citeproc", "--bibliography", str(bib)]
    if csl.exists():
        cmd += ["--csl", str(csl)]
    out = subprocess.run(cmd, input=doc, capture_output=True, text=True, encoding="utf-8", check=True).stdout
    blocks = [b.strip() for b in out.split("\n\n") if b.strip()][1:]   # first block is the in-text "[1] [2] ..."
    return [re.sub(r"^\\\[\d+\\\]\s*", "", b) for b in blocks]


def library_link(key, lib):
    if lib is None or not (lib / "references" / f"{key}.md").exists():
        return ""
    return f" · [{lib.name}](obsidian://open?vault={quote(lib.name)}&file={quote('references/' + key, safe='')})"


def build(text, keys, ids, bib, csl, lib=None):
    base = masked(REFS.sub("", text), lambda t: unnumber(t, ids)).rstrip("\n") + "\n"
    head, body = base.split("\n---\n", 1) if base.startswith("---\n") else ("", base)
    body, order = masked(body, lambda t: number(t, keys))
    if order:
        items = render(order, bib, csl)
        entries = [f"\\[{i}\\] {item}{library_link(k, lib)} ^{block_id(k)}" for i, (k, item) in enumerate(zip(order, items), 1)]
        body = (body.rstrip("\n") + f"\n\n## References\n\n%% refs:start: generated from {bib.name}, do not edit %%\n"
                + "\n\n".join(entries) + "\n%% refs:end %%\n")
    return (head + "\n---\n" + body) if head else body


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--bib")
    ap.add_argument("--library")
    ap.add_argument("--csl", default="_scripts/ieee.csl")
    ap.add_argument("folders", nargs="*", default=["atoms", "molecules"])
    a = ap.parse_args()
    lib = (VAULT / a.library).resolve() if a.library else None
    bib = VAULT / a.bib if a.bib else (lib / "library.bib" if lib else VAULT / "library.bib")
    csl = VAULT / a.csl
    if not bib.exists():
        sys.exit(f"no bibliography at {bib}")
    keys = set(re.findall(r"@\w+\s*\{\s*([^,\s]+)\s*,", bib.read_text(encoding="utf-8")))
    ids = {block_id(k): k for k in keys}
    changed, missing = [], set()
    for folder in a.folders:
        for p in sorted((VAULT / folder).rglob("*.md")):
            text = p.read_text(encoding="utf-8")
            missing |= {k for k in re.findall(r"(?<![\w.])@(" + KEY + r")", masked(text, lambda t: CODE.sub("", t))) if k not in keys}
            new = build(text, keys, ids, bib, csl, lib)
            if new != text:
                changed.append(p.relative_to(VAULT))
                if not a.check:
                    p.write_text(new, encoding="utf-8", newline="\n")
    for p in changed:
        print(("would change " if a.check else "updated ") + str(p))
    if missing:
        print("not in " + bib.name + ": " + ", ".join(sorted(missing)), file=sys.stderr)
    sys.exit(1 if a.check and changed else 0)


if __name__ == "__main__":
    main()
