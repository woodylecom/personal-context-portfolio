# Wiring: Expose Your Portfolio as an MCP Resource

## What This Does

MCP (Model Context Protocol) lets AI tools access external data sources. By exposing your context portfolio as an MCP resource, any MCP-compatible tool can read your files on demand — the agent pulls what it needs rather than you deciding what to paste.

This is the most powerful wiring option because it makes your portfolio automatically available to any agent that supports MCP, without you copying and pasting anything.

## How It Works

Your portfolio is a folder of markdown files. An MCP server exposes that folder as a resource. Any MCP-compatible client (Claude Desktop, Claude Code, OpenClaw, etc.) connects to the server and can read any file in your portfolio.

## Basic Setup

**Option 1: Local MCP server (filesystem)**

If your portfolio lives on your local machine, use the MCP filesystem server to expose the directory.

1. Store your portfolio files in a dedicated folder (e.g., `~/context-portfolio/`)
2. Configure your MCP client to connect to the filesystem server pointing at that directory
3. Any connected AI tool can now read your portfolio files

The exact configuration depends on your MCP client. Check your tool's documentation for how to add an MCP filesystem resource.

### Worked Example: Filesystem MCP Server (Claude Desktop / Claude Code)

Both Claude Desktop and Claude Code read MCP server definitions from a JSON config file. Add an entry pointing at your portfolio folder:

```json
{
  "mcpServers": {
    "context-portfolio": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/absolute/path/to/your/context-portfolio"
      ]
    }
  }
}
```

Where this file lives depends on the client:

- **Claude Desktop:** `claude_desktop_config.json` (Settings → Developer → Edit Config).
- **Claude Code:** `.mcp.json` in your project root for a project-scoped server, or `~/.claude.json` for a server available in every session. See [`claude-code.md`](claude-code.md) for how Claude Code combines this with `CLAUDE.md`.

Restart the client after saving. The agent can now list and read files in that folder on demand — no more pasting file contents into chat.

**Start narrow.** Point the server at a folder that contains just `identity.md`, `role-and-responsibilities.md`, and `current-projects.md` if you don't want to expose everything yet. You can widen the folder (or add a second server pointed at the rest of the portfolio) later. This mirrors the "start with identity + role + projects" guidance below — it applies to what you expose via MCP, not just what you paste into a prompt.

**Option 2: Remote MCP server**

If you want your portfolio accessible from multiple devices or by remote agents, you'll need to serve it from a remote location — a cloud server, a GitHub repo exposed via MCP, or a custom MCP server.

This is a more involved setup. If you're building with Claude Code, you can ask it to help you build a simple MCP server that serves your portfolio files.

## Tips

- Start with the filesystem approach if you're just trying it out. You can move to remote later.
- You don't have to expose all ten files. Start with identity, role, and current projects — those three cover most use cases.
- Update the files in your folder and the MCP resource updates automatically. No redeployment needed.
- Consider access control if you're serving remotely. Your portfolio contains personal and professional information you may not want publicly accessible.

## What to Build Next

Once your portfolio is available via MCP, the natural next step is building agents that read specific files at the start of their workflow. A meeting prep agent that reads `team-and-relationships.md` and `current-projects.md`. A writing assistant that reads `communication-style.md`. A planning agent that reads `goals-and-priorities.md`. The portfolio becomes the context layer that every agent draws from.
