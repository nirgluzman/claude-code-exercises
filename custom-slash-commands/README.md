# [Custom Slash Commands](https://code.claude.com/docs/en/slash-commands#custom-slash-commands)

Allow you to define frequently used prompts as Markdown files that Claude Code can execute.

The "scope" of a custom slash command is determined by its file system location:
- **Personal Scope Global**: Placed in `~/.claude/commands/` folder, available in all projects.
- **Project Scope**: Placed in `[your-project-root]/.claude/commands/` folder. These are scoped only to the current repository.


## [Arguments](https://code.claude.com/docs/en/slash-commands#arguments)

The $ARGUMENTS placeholder captures all arguments passed to the command.


## [Bash Command Execution](https://code.claude.com/docs/en/slash-commands#bash-command-execution)

You can execute `bash` commands before the slash command runs using the `!` prefix. <br />
The output is included in the command context. <br />
You must include `allowed-tools` with the Bash tool, but you can choose the specific bash commands to allow (i.e. limit the tools the Agent can use).
