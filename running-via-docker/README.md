# [Claude Code's Native Sandboxing](https://code.claude.com/docs/en/sandboxing)

Claude Code features native sandboxing to provide a more secure environment for agent execution while reducing the need for constant permission prompts

You can enable sandboxing by running the `/sandbox` command.

# [Running Claude Code via Docker](https://docs.docker.com/ai/sandboxes/claude-code/)

Running Claude Code inside Docker is the gold standard for security and automation. It allows you to give the agent "Full Permissions" to run commands and edit files while ensuring it is safely trapped in a sandbox, away from your host OS.

The most efficient way to do this is using the official **Docker Sandboxes** feature.

```bash
docker sandbox run claude ~/your-project-path
```

This will create a sandboxed container with Claude Code and attach it to your current terminal session.

`~/your-project-path`: The folder on your computer Claude is allowed to see and edit.

You can now use Claude Code as usual, but all commands and file changes will be executed inside the sandboxed container.

To exit the sandboxed container, simply type `exit`.

```bash
docker sandbox run claude ~/your-project-path
docker sandbox exit
```

**Security Tip:**<br/>
You can run `claude --dangerously-skip-permissions` inside this sandbox to work unattended without worrying about your host machine.


```bash
docker sandbox run claude ~/your-project-path claude --dangerously-skip-permissions
docker sandbox exit
```

This is useful for automating workflows, such as running Claude Code as part of a CI/CD pipeline. 
