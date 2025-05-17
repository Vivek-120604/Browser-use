from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("Google_API_KEY")
async def main():
    agent = Agent(
    task="""
    Open YouTube by navigating to 'https://www.youtube.com'. 
    In the search bar, search for 'Think School Budget 2025'. 
    From the search results, click on the first relevant video and start playing it.
    """,
    llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash', api_key=api_key)
)
    result = await agent.run()
    print(result)

asyncio.run(main())