from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")

@mcp.tool()
def get_weather(location:str)->str:
    """
    get the weather location
    """

    return "It's always raining in California"


#transport Protocol
#http

if __name__=="__main__":
    mcp.run(transport="streamable-http")