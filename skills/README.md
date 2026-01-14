# [Agent Skills](https://code.claude.com/docs/en/skills) - Extend Claude’s capabilities

https://agentskills.io/home <br />
[Anthropic's Skills repository](https://github.com/anthropics/skills) <br />
[Claude Skills Marketplace](https://github.com/mhattingpete/claude-skills-marketplace/tree/main) <br />
[Skills announcement](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

***Instructions that extend Claude's knowledge.*** <br />
Skills are modular, reusable knowledge packages (like folders with instructions and code) that provide Claude with specialized expertise, allowing it to autonomously learn and apply domain-specific workflows, best practices, and tools for complex coding tasks, reducing repetitive prompting and transforming general agents into specialists. <br />
These skills are dynamically loaded on-demand, enhancing Claude's capabilities for tasks like data analysis, file processing, or adhering to coding standards.

Claude Skills are like a more advanced, modular **system prompt**, allowing you to package domain-specific knowledge, workflows, and best practices into reusable components (Markdown files) that Claude loads on-demand, reducing bloat and repetition compared to stuffing everything into one large, static system prompt.

Claude skills are primarily **loaded dynamically**. They use a mechanism called "progressive disclosure" to optimize context window usage and ensure efficiency.

## [When to use Skills versus other options](https://code.claude.com/docs/en/skills#when-to-use-skills-versus-other-options )

### [Skills vs. Subagents](https://dev.to/nunc/claude-code-skills-vs-subagents-when-to-use-what-4d12)

- **Context**: Skills add to the main context; Subagents create new, isolated contexts.
- Claude Code spawns subagents ("specialized coworker") to handle modular tasks within complex workflows.
- Use Skills for guidance and standards; use subagents when you need isolation or different tool access.

### Skills vs. MCP

- Skills tell Claude how to use tools; MCP provides the tools.
- For example, an MCP server connects Claude to your database, while a Skill teaches Claude your data model and query patterns.

Before installing/creating a Skill, see what Skills Claude already has access to with: ```What Skills are available?```

## Installing Skills from the Marketplace

1) Clone the marketplace repository into `~/.claude/plugins/marketplaces/`

```bash
/plugin marketplace add anthropics/skills
```

2) Browse and install skills

```bash
/plugin
```

## [Custom Skill](https://code.claude.com/docs/en/skills#create-your-first-skill)

1) Create a new folder in `~/.claude/skills/` with your skill name.
2) Add a `SKILL.md` file with your skill instructions.
3) (Optional) Add additional files or folders as needed for your skill.
4) Skills are automatically loaded when created or modified. <br />Verify the Skill appears in the list with: `What Skills are available?`
