from agents import Agent
from tools import calculator_tools

agent = Agent(
    "You are a helpful assistant tasked with performing arithmetic on a set of inputs.",
    calculator_tools,
)


def set_api_key(api_key):
    agent.set_api_key(api_key)
    return ""


def response(messages):
    try:
        config = {"configurable": {"thread_id": "1"}}
        messages = agent.get_agent().invoke({"messages": messages}, config=config)
        return "", "\n".join([m.pretty_repr() for m in messages["messages"]])
    except Exception as e:
        print(e)
        return "", "There is somenthing wrong with your api key"
