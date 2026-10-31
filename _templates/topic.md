---
type: topic
title: "{{title}}"
parent: ""
created: {{date:YYYY-MM-DD}}
updated: {{date:YYYY-MM-DD}}
visibility: shared
---

# {{title}}

## Sub-hubs

```dataview
LIST FROM "topics" WHERE parent = this.file.link SORT file.name ASC
```

## Atoms

```dataview
LIST FROM [[]] AND "atoms" SORT file.name ASC
```

## Molecules

```dataview
LIST FROM [[]] AND "molecules" SORT file.name ASC
```

## Sources

```dataview
LIST FROM [[]] AND "sources" SORT read DESC
```


