from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.youtube_tools import YouTubeTools
from config.settings import get_google_api_key

def create_youtube_agent():
    return Agent(
        name="YouTubeTimestampAgent",
        model=Gemini(
            model="gemini-1.5-flash",
            api_key=get_google_api_key()
        ),
        tools=[YouTubeTools()],
        show_tools_calls=True,
        instructions=[
            "Analyze YouTube video content thoroughly.",
            "Generate accurate timestamps in [start, end, summary] format.",
            "Verify video length before creating timestamps.",
            "Never invent or guess timestamps."
        ]
    )