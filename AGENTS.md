# AGENTS.md

Conventions for this vault, for humans and agents, based on **Molecular Notes** by Robert Martin (https://github.com/robertmartin8/MolecularNotes).

If `AGENTS.local.md` exists, read it next; it wins where the two differ.

## The noun rule

> **Atoms are nouns. Molecules are claims.**

An atom is a thing with a name: a concept, technique, method, role, document, event, organization or skill. Test: could the title be a Wikipedia article or a glossary entry? If the title asserts something, it's a molecule.

## Atoms

- **Relevance first:** the opening sentence says why the concept matters, then the definition.
- **End on the tension or implication.** Report disagreement between sources; don't adjudicate it.
- Background not found in any source is marked `(general reference)`.

## Style modules

Swappable modules in `_style/`. Read the ones this vault uses before writing.

| Module | Choice | Default |
|---|---|---|
| Atom extraction | `_style/Atom Extraction.md` | always |
| Atom shape | `_style/Atoms - Short.md` or `_style/Atoms - Full.md` | Short |
| Molecules | `_style/Molecules.md` | always |
| Voice | `_style/Voice - Plain.md` or `_style/Voice - Scientific.md` | Plain |

## Citations

Every quote is verbatim from a source note and links the heading it sits under: `"…quoted text…" ([[Source Note#Heading]])`. Use straight outer quotes by default; curly outer quotes (“…”) when the quote itself contains straight quotes. With a BibTeX library (`library.bib` at the vault root), cite books and papers in prose with pandoc keys, `[@kolda2009tensor]`; `python3 _scripts/build_references.py` numbers them and writes each note's `## References`.

## Topics

Hubs are built from `_templates/topic.md`: a one-line scope and an **Excludes** line above the template's Dataview lists (never hand-written member lists).

- Start with one hub per area.
- A hub that reaches ~25 notes splits into sub-hubs; each names its hub in `parent:`.
- A note lists its most specific hub in `topics:`, not the parent as well.
- A hub under ~3 notes merges back into its parent.

## Note types

```
atoms/      nouns: concepts derived from sources, one each
molecules/  your own thinking, in kinds (see _style/Molecules.md)
topics/     hubs that group atoms and molecules
sources/    notes on media: books, papers, articles, videos, podcasts
_style/     style modules: atom extraction, atom shape, molecules, voice
```

## Frontmatter

Common to all notes: `type`, `title`, `topics`, `created`, `updated`, `visibility`.

```yaml
# Atom
type: atom
title: ""
aliases: []         # optional: other spellings, acronyms
topics: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: []          # [[wikilinks]] to every source note quoted
visibility: shared

# Molecule
type: molecule
kind: claim         # claim | list | comparison | discussion | survey | campaign | requirements
title: ""
topics: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
atoms: []           # [[wikilinks]] to the atoms it builds on
visibility: shared

# Topic
type: topic
title: ""
parent: ""          # optional: [[parent hub]] for a sub-hub
created: YYYY-MM-DD
updated: YYYY-MM-DD
visibility: shared

# Source
type: source
title: ""
author: ""
kind: book          # book | paper | article | post | video | podcast | course
url: ""
topics: []
created: YYYY-MM-DD
read: YYYY-MM-DD
visibility: shared
```

## ideas/ (optional)

A vault may have an `ideas/` folder — a lightweight backlog for things worth exploring here later. It's self-contained: see `ideas/AGENTS.md` if present. Absent means this vault hasn't opted in.

## skills/ (optional)

A vault may ship its own `skills/<name>/SKILL.md` files — agent skills that travel with the vault in git. `skills/brain-ideas/SKILL.md` operates on `ideas/` if present. Removing one doesn't remove the other; clean up both when retiring a feature.

## visibility

`shared` (default) · `private` (never leaves this vault) · `restricted` (only vaults listed in a `share_with: []` field). Nothing syncs automatically — this just records intent.

## Conventions

- Wikilinks (`[[ ]]`) inside the vault, not Markdown links.
- Topics group; explanation lives in atoms and molecules.
