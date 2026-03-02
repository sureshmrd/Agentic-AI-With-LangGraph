from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math") #server

#tools in server
@mcp.tool()
def add(a:int,b:int)->int:
    """
    add two numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int,b:int)->int:
    """
    multiply two numbers
    """
    return a*b

#transport-protocol
# stdio : standard input-output to recieve and respond to tool function calls.

if __name__=="__main__":
    mcp.run(transport = "stdio")

