# Second Brain — Molecular Notes (clean)

A minimal Obsidian vault built on **Molecular Notes** by Robert Martin: https://github.com/robertmartin8/MolecularNotes (philosophy: [part 1](https://reasonabledeviations.com/2022/04/18/molecular-notes-part-1/), [part 2](https://reasonabledeviations.com/2022/06/12/molecular-notes-part-2/)), for you and AI agents alike. Conventions are in `AGENTS.md`.

Changes from the original:

- types in YAML frontmatter instead of tags, so agents and Dataview read them reliably;
- a `visibility` field (`shared`, `private`, `restricted`) marking whether a note may be copied into other vaults;
- atoms are nouns, molecules are claims, and molecules come in kinds;
- quotes are verbatim and link the source-note heading they come from;
- swappable style modules in `_style/`.

Plugins: Dataview and Templater.

## Start

1. Open this folder in [Obsidian](https://obsidian.md) as a vault.
2. Enable the community plugins when prompted.
3. Write your first **source** note, pull an **atom** from it, build a **molecule** on atoms, group them under a **topic**.
4. Citing papers: put your BibTeX file at `library.bib`, cite `[@key]`, run `python3 _scripts/build_references.py` (needs [pandoc](https://pandoc.org)).

A placeholder of each note type is included — [[Example Topic]], [[Example Source]], [[Example Atom]], [[Example Molecule]] — so the graph has something to render on first open. Delete them once you've started.

## Graph colors

`.obsidian/graph.json` is not tracked: it also stores per-session view state (zoom, pan, search) that would show up as diffs. After cloning, restore the color groups for `atoms/`, `molecules/`, `topics/`, `sources/` once:

```sh
python3 _scripts/restore_graph_colors.py .
```

(`_scripts/restore-graph-colors.ps1` does the same in PowerShell.)
