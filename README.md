# hnsum
Summarize Hacker News with AI!

## Conversational Hacker News

Barebones example of using the [Model Context Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol) to make the top [Hacker News](https://news.ycombinator.com) stories available to LLM applications like Claude.

## Usage (Claude Plus/Pro only)

Clone the repository locally and update the [Claude Desktop App](https://claude.ai/download) and update the config file to include the MCP server:

```json
{
  "mcpServers": {
    "hacker-news": {
      "command": "/path/to/hnsum/.venv/bin/python3",
      "args": ["/path/to/hnsum/server.py"]
    }
  }
}
```

Note: The above config example assumes you've preconfigured a virtual environment to obtain the python dependencies.

Now restart the Claude desktop app and the `hacker-news` tool should show up under the "Search and tools" dropdown. Ensure it's enabled, then prompt Claude with something regarding the site. Claude will ask permission before invoking the tool to respond.
