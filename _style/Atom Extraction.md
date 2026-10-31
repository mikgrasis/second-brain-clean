---
type: guide
title: "Atom Extraction"
visibility: shared
---

# Atom Extraction

How atoms get pulled out of sources, by you or by an agent you hand a batch to.

## The flow

1. **Source note first.** Every atom is extracted from one or more source notes in `sources/`. Extraction is progressive: the notes you need now, not a bulk pass over everything.
2. **Pick the nouns.** List the concepts the source actually explains — a definition, a property, a mechanism, a caveat — not ones it only names in passing.
3. **Check what exists.** Search `atoms/` first; extend an existing atom rather than duplicating it. Keep the planned atoms in a list (e.g. `_fixups/atom-inventory.md`) when a source yields many.
4. **Skip the thin ones.** A concept with fewer than two substantive statements in the sources doesn't get an atom yet.
5. **Reference atoms.** Before a batch, write or pick two or three atoms that show the vault's shape and voice. Every writer reads them first.
6. **Write**, one file per atom, in the vault's atom shape and voice.
7. **Check:** every quote verbatim in its source note, every link resolves.
8. **Link:** the atom names its hubs in `topics:`; molecules that build on it list it in `atoms:`.

## Naming

Singular, no article, a parenthetical only to disambiguate: *Rank (tensor)*. Other spellings and acronyms go in `aliases:`.

## Briefing an agent

Hand over: the atom titles to write, the source notes they come from, the reference atoms, the modules this vault uses, and these boundaries:

- Write only the assigned files in `atoms/`. Never edit source notes, existing atoms or `AGENTS.md`.
- Run the check before finishing.
- Report skipped concepts and why, and any source errors found.
- Don't commit; whoever integrates the batch does.
