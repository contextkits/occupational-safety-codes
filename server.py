from mcp.server.fastmcp import FastMCP

# CHANGE THIS NAME FOR EACH REPO (e.g., "maritime-vessel-specs")
mcp = FastMCP("CHANGE-ME-TO-REPO-NAME")

@mcp.tool()
def lookup_code(code: str) -> str:
    """
    Look up a standard industry code or specification.
    """
    # This is a placeholder for the live database.
    # In production, this connects to the full dataset.
    return f"Lookup service for {code} is active. Database connection ready."

if __name__ == "__main__":
    mcp.run()
