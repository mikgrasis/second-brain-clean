# Second Brain — Molecular Notes (clean)

A minimal Obsidian vault implementing **Molecular Notes** by Robert Martin: https://github.com/robertmartin8/MolecularNotes (philosophy: [part 1](https://reasonabledeviations.com/2022/04/18/molecular-notes-part-1/), [part 2](https://reasonabledeviations.com/2022/06/12/molecular-notes-part-2/)).

Four note types: **atoms** (knowledge from a source), **molecules** (your own permanent notes), **topics** (groupings), **sources** (media notes). Conventions and the frontmatter schema are in `AGENTS.md`.

Changes from the original: types in YAML frontmatter instead of tags, and a `visibility` field so the vault can coexist with other brains. Plugins: Dataview and Templater.

## Start

1. Open this folder in [Obsidian](https://obsidian.md) as a vault.
2. Enable the community plugins when prompted.
3. Write your first **source** note, pull an **atom** from it, connect atoms into a **molecule**, group them under a **topic**.

A placeholder example of each note type is included — [[Example Topic]], [[Example Source]], [[Example Atom]], [[Example Molecule]] — so the graph view has something to render on first open. Delete these once you've started your own vault.

## Graph colors

`.obsidian/graph.json` is tracked so the vault ships with color groups for `atoms/`, `molecules/`, `topics/`, `sources/` already set up. After cloning, mark it as "skip worktree" so your local zoom/pan/search changes don't show up as diffs:

```sh
git update-index --skip-worktree .obsidian/graph.json
```
