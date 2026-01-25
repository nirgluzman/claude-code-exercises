# [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)

MCP (Model Context Protocol) is an open standard that allows AI systems to connect with external tools and data sources.

## [PulseMCP](https://www.pulsemcp.com/)

Community-driven hub and ecosystem tracker for the MCP.


## [Context7](https://context7.com/) - Up-to-date Docs

Documentation service that provides up-to-date, version-specific code examples and documentation directly to LLMs and AI coding tools (like Cursor, VS Code, Claude).

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --scope project
```

It is recommended that MCP preferences be added to `CLAUDE.md` (project's persistent configuration and instruction set) to ensure the MCP is utilized by default.

## Context Efficiency & MCP Integration

Context usage refers to the total volume of tokens (code, file content, and tool definitions) that Claude processes within a single session. <br />
Because this context has a finite capacity (e.g., 200k tokens), managing it efficiently ensures Claude remains fast and accurate.
<br />
To see exactly how much memory is being used and which files or tools are consuming the most space, the following slash command should be used:

```bash
/context
```

To ensure a streamlined environment, the active MCP configuration should be audited using the following command:

```bash
claude mcp list
```

This command displays all currently integrated MCP servers, allowing users to identify and remove any that are not essential to the current project.

To remove an unnecessary MCP server, use the command:

```bash
claude mcp remove <mcp_name>
```

To start claude with specific MCP server, use this command:

```bash
claude --mcp-config <mcp config file> --strict-mcp-config
```
