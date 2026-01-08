# [Memory](https://code.claude.com/docs/en/memory)

## General

`CLAUDE.md` is a special file that Claude automatically pulls into context when starting a conversation.

`/init` - Initialize a new `CLAUDE.md` file with codebase documentation.

* All memory files are automatically loaded into Claude Code’s context when launched.
* Files higher in the hierarchy take precedence and are loaded first, providing a foundation that more specific memories build upon.

## Conditional Context Loading

* Dynamically update context based on git branch.
* Smart context switching with hooks - analyze user input to load appropriate context.
