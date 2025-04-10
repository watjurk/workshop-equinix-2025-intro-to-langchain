import getpass
import os

from dotenv import load_dotenv
from IPython.display import Image, display
from langchain.chat_models import init_chat_model
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent

from lib import init_stdout_log_saver, prompt_graph, save_graph_as_png, show_graph

load_dotenv()


if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")


model = init_chat_model("qwen-qwq-32b", model_provider="groq", temperature=0)


wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())  # type: ignore - This is pylance being just silly
tools = [wikipedia]

memory = InMemorySaver()
graph = create_react_agent(
    model,
    tools=tools,
    checkpointer=memory,
)

show_graph(graph)
save_graph_as_png(graph)

thread_id = 1
init_stdout_log_saver(thread_id)
while True:
    prompt = input("Enter a prompt: ")
    if prompt == "exit":
        break

    prompt_graph(graph, thread_id, prompt)
    print("\n\n\n\n")
