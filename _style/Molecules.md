---
type: guide
title: "Molecules"
visibility: shared
---

# Molecules

A molecule is your own thinking, built from atoms. Its `kind` says its shape; the default is `claim`.

| `kind` | Title | Shape |
|---|---|---|
| `claim` | the claim itself: *Spaced Repetition Beats Cramming for Retention* | Prose, no headings: the claim and its evidence, the counter-case (required when anything cuts the other way), what follows. |
| `list` | what's listed and for what: *Reading List - Foundations of Ecology* | A short intro saying what got on the list and why, then the items, each with its reason and links. |
| `comparison` | the things compared: *Zettelkasten vs. PARA for Personal Notes* | The question, a table or per-option paragraphs on the same criteria, then the verdict and when it flips. |
| `discussion` | the open question: *Should Notes Be Written for a Future Reader* | The question, each candidate outcome with what supports and undercuts it, what would settle it, the current lean. |
| `survey` | the field and its date: *State of the Art in Tensor Completion (2026)* | Where the field stands, the main lines of work with their best results, what's open. Dated; revise rather than append. |
| `campaign` | the effort: *Campaign Plan (Kitchen Garden 2026)* | Goal, steps or phases with status, what was learned, next action. A living note; history stays in git. |
| `requirements` | what's needed for what: *Data Requirements for a Bird-Count Study* | What the work needs (data, tools, access), what's already held and what's missing, where each gap is tracked. |

- All kinds except `claim` may use headings.
- All kinds cite like atoms and list the atoms they build on in `atoms:`.
- Pick the smallest kind that fits; a list of one claim is a claim.
