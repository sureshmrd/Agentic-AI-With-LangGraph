from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_groq import ChatGroq
from langchain.agents import create_agent

from dotenv import load_dotenv
load_dotenv()

import asyncio
import os

async def main():
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.1-8b-instant")
    
    # Create agent with proper initialization
    agent = create_agent(model, tools)

    try:
        math_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
        )
        # Extract content from the last message
        if 'messages' in math_response:
            last_msg = math_response['messages'][-1]
            print("Math response:", last_msg.content if hasattr(last_msg, 'content') else last_msg)
        else:
            print("Math response:", math_response)
    except Exception as e:
        print(f"Math request failed: {type(e).__name__}: {str(e)}")

    try:
        weather_response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": "what is the weather in California?"}]}
        )
        # Extract content from the last message
        if 'messages' in weather_response:
            last_msg = weather_response['messages'][-1]
            print("Weather response:", last_msg.content if hasattr(last_msg, 'content') else last_msg)
        else:
            print("Weather response:", weather_response)
    except Exception as e:
        print(f"Weather request failed: {type(e).__name__}: {str(e)}")

asyncio.run(main())
