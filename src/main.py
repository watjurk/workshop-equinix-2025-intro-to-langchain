import getpass
import os

try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

from langchain.chat_models import init_chat_model
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

# Chatbot initialization
model = init_chat_model("deepseek-r1-distill-qwen-32b", model_provider="groq")

# Tool used to extract information from wikipedia
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())  # type: ignore - This is pylance being just silly

# @tool
# def check_weather(location: str) -> str:
#     """This tool returns the weather forecast for the specified location."""
#     return f"Now it's sunny in {location}"


# tools = [check_weather]

# List of all tools available to the LLM
tools = [wikipedia]

# Environment where the model interacts with the tools
graph = create_react_agent(model, tools=tools)

inputs = {"messages": [("user", "What is Hunter x Hunter?")]}
for s in graph.stream(inputs, stream_mode="values"):
    message = s["messages"][-1]
    if isinstance(message, tuple):
        print(message)
    else:
        message.pretty_print()
