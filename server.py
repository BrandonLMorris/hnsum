#!/usr/bin/env python3
from fetch import top_stories as fetch_top_stories

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("hacker-news")

@mcp.tool("top_stories")
def top_stories() -> str:
    """
    Get details objects for the top Hacker News stories.
    
    Args:
        limit (int): The number of top stories to retrieve.
    
    Returns:
        str: A string of JSON objects representing the top stories.
    """
    return str(fetch_top_stories())


if __name__ == "__main__":
    mcp.run(transport='stdio')
