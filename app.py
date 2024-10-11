from agents import Agent
from tools import calculator_tools

agent = Agent(
    "You are a helpful assistant tasked with performing arithmetic on a set of inputs.",
    calculator_tools,
)


def set_api_key(api_key):
    agent.set_api_key(api_key)


def response(messages):
    messages = agent.get_agent().invoke({"messages": messages})
    return "\n".join([m.pretty_repr() for m in messages['messages']])