# [Output Styles](https://code.claude.com/docs/en/output-styles)

Feature that lets you change the AI's core personality and communication style by modifying its system prompt, enabling it to act as different specialized agents while retaining tools like file manipulation and script execution.

---
**NOTE**: <br />
The `/output-style:new` command and the broader "output styles" feature in Claude Code have been marked as deprecated by Anthropic, with a transition towards using plugins and other prompt engineering methods.

## Built-in Output Styles

- **Default**
- **Explanatory**: Provides educational “Insights” in between helping you complete software engineering tasks.
- **Learning**: Collaborative, learn-by-doing mode where Claude will not only share “Insights” while coding, but also ask you to contribute small, strategic pieces of code yourself.

## Customize the Output Style

- `/output-style` to access a menu and select your output style.
- `/output-style [style]` to directly switch to a style.

You can also create your own custom output styles by defining a new system prompt that tailors the AI's behavior to your specific needs.
