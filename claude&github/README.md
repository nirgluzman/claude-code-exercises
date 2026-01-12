# [Integrating Claude Code with GitHub](https://code.claude.com/docs/en/github-actions)

Claude Code GitHub Actions brings AI-powered automation to your GitHub workflow. <br />
With a simple `@claude` mention in any PR or issue, Claude can analyze your code, create pull requests, implement features, and fix bugs - all while following your project’s standards.

## Setup

Open claude and run `/install-github-app` <br />
This command will guide you through setting up the GitHub app and required secrets.

## Usage
Once the GitHub app is installed, you can start using Claude in your pull requests and issues. <br />
Simply mention `@claude` followed by your request. For example:
- `@claude implement this feature based on the issue description.`
- `@claude how should I implement user authentication for this endpoint?`
- `@claude fix the TypeError in the user dashboard component.`


Claude will respond directly in the thread with its analysis or changes.

## Important Note

To ensure Claude is provided with the necessary project context, the repository root must include `CLAUDE.md`.
