from langgraph.graph.graph import CompiledGraph
from langchain_core.runnables import RunnableConfig


def prompt_graph(graph: CompiledGraph, thread_id: int, prompt: str):
    inputs = {"messages": [("user", prompt)]}
    config: RunnableConfig = {"configurable": {"thread_id": "1"}}
    for s in graph.stream(inputs, config=config, stream_mode="values"):
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


# from langchain_core.tools import tool
# @tool
# def check_weather(location: str) -> str:
#     """This tool returns the weather forecast for the specified location."""
#     return f"Now it's sunny in {location}"

# tools = [check_weather]
