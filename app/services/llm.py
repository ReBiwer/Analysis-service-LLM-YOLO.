from logging import Logger
from typing import TypedDict

from httpx import AsyncClient, Client
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph

from app.config import settings


class State(TypedDict):
    query: str
    objects: list[str]
    response: str


class LLMService:
    model_name = "gpt-4o-mini"

    def __init__(self, logger: Logger):
        self.logger = logger
        self.model = ChatOpenAI(
            model=self.model_name,
            temperature=0.7,
            api_key=settings.OPENAI_API_KEY,
            http_client=Client(proxy=settings.PROXY_URL),
            http_async_client=AsyncClient(proxy=settings.PROXY_URL)
        )
        self.prompt = PromptTemplate(
            input_variables=["query", "objects"],
            template="Ответь на вопрос пользователя {query} касательно этих объектов: {objects}"
        )
        workflow = StateGraph(State)
        workflow.add_node("invoke_node", self._invoke_node)
        workflow.set_entry_point("invoke_node")
        self.graph = workflow.compile()


    def _invoke_node(self, state: State):
        message = HumanMessage(
            content=self.prompt.format(
                query=state["query"],
                objects=', '.join(state["objects"])
            )
        )
        response = self.model.invoke([message]).content
        return {"response": response}


    def get_response(self, query: str, objects: list[str]) -> str:
        result = self.graph.invoke({"query": query, "objects": objects})
        return result.get("response")
