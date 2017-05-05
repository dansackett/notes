# Notes

This is the script I use to generate my personal notebook. It allows me to add
new files easily and setup the notebook on any machine quickly. To get started
run:

```
python init.py
```

This will build the notebook in `/$HOME/notes`. The current hierarchy is:

```
notes
├── notes.md
├── scratch.md
├── personal
│   ├── concerns.md
│   ├── goals.md
│   ├── ideas.md
│   ├── relationships.md
│   └── todo.md
└── work
    ├── concerns.md
    ├── goals.md
    ├── ideas.md
    ├── relationships.md
    └── todo.md
```

# Concept

This is based off my coworkers workflow to some degree. Most everything I need
to write down will go to `scratch` or the root `notes` files. Once the writing
is captured it is moved into the work or personal directories filed where it
makes most sense. Sometimes notes aren't meant to be long-lived and in that
case they never move into a sub directory.
