import sys

from langgraph.graph.graph import CompiledGraph


def save_graph_as_png(graph: CompiledGraph):
    png_bytes = graph.get_graph().draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(png_bytes)


def show_graph(graph: CompiledGraph):
    print(graph.get_graph().draw_ascii())


def init_stdout_log_saver(thread_id: int):
    log_file_name = f"logs/log_{thread_id}.txt"

    class Logger(object):
        def __init__(self):
            self.terminal = sys.stdout
            self.log = open(log_file_name, "a")

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)

        def flush(self):
            self.terminal.flush()
            self.log.flush()

    sys.stdout = Logger()


# from langchain_core.tools import tool
# @tool
# def check_weather(location: str) -> str:
#     """This tool returns the weather forecast for the specified location."""
#     return f"Now it's sunny in {location}"

# tools = [check_weather]
