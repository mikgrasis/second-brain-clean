# AGENTS.md

Conventions for this vault, for humans and agents. It implements **Molecular Notes** by Robert Martin (https://github.com/robertmartin8/MolecularNotes), with two deliberate changes: types are declared in **YAML frontmatter** (not tags) so agents and Dataview parse them reliably, and a `visibility` field marks what may be shared with other brains.

## The noun rule

> **Atoms are nouns. Molecules are claims.** (portfolio style since 2026-09-30, from `draft/pkm-brain-light` and `career-brain`)

An atom is a thing with a name: a role, document, technique, event, organization or skill. Test: could the title be a Wikipedia article or a glossary entry? If the title asserts something, it is a molecule.

- **Atoms are prose, relevance first.** Open with why the thing matters to the reader (a hook, not a definition), fold the definition into the first paragraph, then report what the sources say with verbatim quotes woven into sentences, each followed by `([Tag] § Anchor)`. End on the tension or implication. Two to four paragraphs, then `## Related`. Atoms report disagreement between sources; they don't adjudicate it.
- **Molecules are prose too**, titled as a claim: the claim and its evidence, then the counter-case (required when anything cuts the other way), then what follows. No section headings.
- Every cited quote must appear verbatim in the tagged source note. Straight outer quotes by default; curly outer quotes (“…”) when the quote itself contains straight quotes.
- Naming: singular, no article, parenthetical to disambiguate.
- Background not found in any source is marked as general reference in the discussion.

### Evidence tags

Record every tag you use in a table here and in `_scripts/quote_tags.json` (tag → file holding the quoted text, relative to the vault; copy outside evidence into `_evidence/`). Check with `python3 ../tooling/quote_check.py . _scripts/quote_tags.json`.

## Top-level topics

Hubs are built from `_templates/topic.md`: a one-line scope and an **Excludes** line above the template's Dataview lists (never hand-written member lists).

## Note types

```
atoms/      knowledge derived from a source — one idea each
molecules/  your own observations and permanent notes
topics/     category notes — group related atoms/molecules
sources/    notes on any media: books, articles, papers, videos
```

## Frontmatter

Common to all notes: `type`, `title`, `topics`, `created`, `updated`, `visibility`.

```yaml
# Atom
type: atom
title: ""
topics: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: []          # [[wikilinks]] to sources/
visibility: shared

# Molecule
type: molecule
title: ""
topics: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
atoms: []           # [[wikilinks]] to atoms it connects
visibility: shared

# Topic
type: topic
title: ""
created: YYYY-MM-DD
updated: YYYY-MM-DD
visibility: shared

# Source
type: source
title: ""
author: ""
kind: book          # book | article | paper | post | video | podcast | course
url: ""
topics: []
created: YYYY-MM-DD
read: YYYY-MM-DD
visibility: shared
```

## ideas/ (optional)

A brain may have an `ideas/` folder — a lightweight backlog for things worth exploring
here later. It's self-contained: see `ideas/AGENTS.md` if present. Absent means this
brain hasn't opted in; nothing else in this file depends on it either way.

## skills/ (optional)

A brain may ship its own `skills/<name>/SKILL.md` files — per-brain skills that travel
with the vault in git, rather than living only in an account's installed-skills list.
`skills/brain-ideas/SKILL.md` operates on `ideas/` if present. These two folders are
registered independently: removing `ideas/` doesn't remove `skills/brain-ideas/`, and
vice versa — clean up both if fully retiring a feature.

## visibility

`shared` (default) · `private` (never leaves this vault) · `restricted` (only brains in a `share_with: []` field). Nothing syncs automatically — this just records intent.

## Conventions

- Wikilinks (`[[ ]]`), not markdown links.
- One concept per atom.
- Topics are for grouping; keep explanation in the atoms/molecules.
