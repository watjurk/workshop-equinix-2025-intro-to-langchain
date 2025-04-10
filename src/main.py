import getpass
import os

from dotenv import load_dotenv

from lib import init_stdout_log_saver, save_graph_as_png, show_graph

# load environment variables (the API key)
load_dotenv()
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Chatbot initialization

# Tool used to extract information from wikipedia

# All tools available to the agent

# Memory of previous prompts and responses


# Agent that will be tasked with answering questions

# show_graph(graph)
# save_graph_as_png(graph)

# Id of the conversation with the agent
thread_id = 1

# Local logs of conversations
init_stdout_log_saver(thread_id)

# Use our graph to produce an output

# Get the last message - the answer to the prompt

# Print the message with formatting
