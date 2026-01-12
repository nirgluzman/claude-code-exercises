# [Connect Claude Code to tools via MCP](https://code.claude.com/docs/en/mcp)

MCP (Model Context Protocol) is an open standard that allows AI systems to connect with external tools and data sources.

## [Context7](https://context7.com/) - Up-to-date Docs

Documentation service that provides up-to-date, version-specific code examples and documentation directly to LLMs and AI coding tools (like Cursor, VS Code, Claude).

```bash
claude mcp add --transport http context7 https://mcp.context7.com/mcp --scope project
```

It is recommended that MCP preferences be added to `CLAUDE.md` (project's persistent configuration and instruction set) to ensure the MCP is utilized by default.
