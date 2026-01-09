# [Custom Slash Commands](https://code.claude.com/docs/en/slash-commands#custom-slash-commands)

Allow you to define frequently used prompts as Markdown files that Claude Code can execute.

The "scope" of a custom slash command is determined by its file system location:
- **Personal Scope Global**: Placed in `~/.claude/commands/` folder, available in all projects.
- **Project Scope**: Placed in `[your-project-root]/.claude/commands/` folder. These are scoped only to the current repository.


## [Arguments](https://code.claude.com/docs/en/slash-commands#arguments)

The $ARGUMENTS placeholder captures all arguments passed to the command.
