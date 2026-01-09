# Commit Code

**Task:** Generate a professional one-line git commit command based on the staged diff and user hints.

**Logic Flow:**
1. **Analyze Diff:** Identify the specific technical changes in the staged files.
2. **Synthesize:** Combine the user hint (**$ARGUMENTS**) with the technical "what".
3. **Format:** `<type>: <$ARGUMENTS context> - <technical change>`

**Rules:**
- **One Line Only:** Do not generate a commit body or multiple lines.
- **Strict Subject:** Use **$ARGUMENTS** to drive the start of the message. If empty, infer the business logic.
- **Convention:** Use standard types: `feat`, `fix`, `refactor`, `chore`, `docs`.
- **Constraint:** Keep the entire message under 72 characters.
