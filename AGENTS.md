# AGENTS.md

Conventions for this vault, for humans and agents. It implements **Molecular Notes** by
Robert Martin (https://github.com/robertmartin8/MolecularNotes), with two deliberate
changes: types are declared in **YAML frontmatter** (not tags) so agents and Dataview
parse them reliably, and a `visibility` field marks what may be shared with other brains.

## Note types

```
Atoms/      knowledge derived from a source — one idea each
Molecules/  your own observations and permanent notes
Topics/     category notes — group related atoms/molecules
Sources/    notes on any media: books, articles, papers, videos
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
source: []          # [[wikilinks]] to Sources/
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

## visibility

`shared` (default) · `private` (never leaves this vault) · `restricted` (only brains in
a `share_with: []` field). Nothing syncs automatically — this just records intent.

## Conventions

- Wikilinks (`[[ ]]`), not markdown links.
- One concept per atom.
- Topics are for grouping; keep explanation in the atoms/molecules.
