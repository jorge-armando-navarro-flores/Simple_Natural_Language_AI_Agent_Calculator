import os
from langgraph.graph import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode


class Agent:
    def __init__(self, sys_msg, tools):
        self.sys_msg = SystemMessage(sys_msg)
        self.llm = ChatOpenAI(model="gpt-4o")
        self.tools = tools
        self.llm_with_tools = self.llm.bind_tools(self.tools)

    def set_api_key(self, api_key):
        os.environ["OPENAI_API_KEY"] = api_key
        self.llm = ChatOpenAI(model="gpt-4o")
        self.llm_with_tools = self.llm.bind_tools(self.tools)
        
    def assistant(self, state: MessagesState):
        return {
            "messages": [self.llm_with_tools.invoke([self.sys_msg] + state["messages"])]
        }

    def get_agent(self):
        # Graph
        builder = StateGraph(MessagesState)

        # Define nodes: these do the work
        builder.add_node("assistant", self.assistant)
        builder.add_node("tools", ToolNode(self.tools))

        # Define edges: these determine how the control flow moves
        builder.add_edge(START, "assistant")
        builder.add_conditional_edges(
            "assistant",
            # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
            # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
            tools_condition,
        )
        builder.add_edge("tools", "assistant")
        return builder.compile()



class Chain:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")
        self.parser = StrOutputParser()

    def set_chain(self, api_key):
        os.environ["OPENAI_API_KEY"] = api_key
        self.llm = ChatOpenAI(model="gpt-4o")

    def get_chain(self):
        return self.llm | self.parser
