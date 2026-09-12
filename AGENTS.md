# AGENTS.md

Conventions for this vault, for humans and agents. It implements **Molecular Notes** by Robert Martin (https://github.com/robertmartin8/MolecularNotes), with two deliberate changes: types are declared in **YAML frontmatter** (not tags) so agents and Dataview parse them reliably, and a `visibility` field marks what may be shared with other brains.

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
