import getpass
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import create_react_agent

from lib import init_stdout_log_saver, save_graph_as_png, show_graph

# load environment variables (the API key)
load_dotenv()
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Chatbot initialization
model = init_chat_model("qwen-qwq-32b", model_provider="groq", temperature=0)

# Tool used to extract information from wikipedia
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())  # type: ignore - This is pylance being just silly

# All tools available to the agent
tools = [wikipedia]
# Memory of previous prompts and responses
memory = InMemorySaver()

# Agent that will be tasked with answering questions
graph = create_react_agent(
    model,
    tools=tools,
    checkpointer=memory,
)

# show_graph(graph)
# save_graph_as_png(graph)

# Id of the conversation with the agent
thread_id = 1

# Local logs of conversations
init_stdout_log_saver(thread_id)

while True:
    prompt = input("Enter a prompt: ")
    if prompt == "exit":
        break

    # Use our graph to produce an output
    inputs = {"messages": [("user", prompt)]}
    config: RunnableConfig = {"configurable": {"thread_id": thread_id}}
    for s in graph.stream(inputs, config=config, stream_mode="values"):
        # Get the last message - the answer to the prompt
        message = s["messages"][-1]

        # Print the message with formatting
        message.pretty_print()

    print("\n\n\n\n")
