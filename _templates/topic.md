---
type: topic
title: "{{title}}"
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
visibility: shared
---

# {{title}}

## Atoms

```dataview
LIST FROM "Atoms" WHERE contains(topics, this.file.name) SORT file.name ASC
```

## Molecules

```dataview
LIST FROM "Molecules" WHERE contains(topics, this.file.name) SORT file.name ASC
```

## Sources

```dataview
LIST FROM "Sources" WHERE contains(topics, this.file.name) SORT read DESC
```
