import getpass
import os

from langchain.chat_models import init_chat_model
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver
from lib import prompt_graph

try:
    # load environment variables from .env file (requires `python-dotenv`)
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")


model = init_chat_model("qwen-qwq-32b", model_provider="groq")


wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())  # type: ignore - This is pylance being just silly
tools = [wikipedia]

memory = InMemorySaver()
graph = create_react_agent(
    model,
    tools=tools,
    checkpointer=memory,
)

thread_id = 1
while True:
    prompt = input("Enter a prompt: ")
    if prompt == "exit":
        break

    prompt_graph(graph, thread_id, prompt)
    print("\n\n\n\n")
