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
LIST FROM "atoms" WHERE contains(topics, this.file.name) SORT file.name ASC
```

## Molecules

```dataview
LIST FROM "molecules" WHERE contains(topics, this.file.name) SORT file.name ASC
```

## Sources

```dataview
LIST FROM "sources" WHERE contains(topics, this.file.name) SORT read DESC
```
