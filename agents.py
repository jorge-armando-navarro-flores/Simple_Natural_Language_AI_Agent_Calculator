import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


class Chain:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o")
        self.parser = StrOutputParser()

    def set_chain(self, api_key):
        os.environ["OPENAI_API_KEY"] = api_key
        self.llm = ChatOpenAI(model="gpt-4o")

    def get_chain(self):
        return self.llm | self.parser
