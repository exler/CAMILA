from typing import Self

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory

from camila.settings import Settings
from camila.store import Store


class Chain:
    def __init__(self: Self, settings: Settings, store: Store) -> None:
        self._settings = settings
        self._llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=settings.OPENAI_API_KEY)

        self._memory = ConversationSummaryMemory(llm=self._llm, memory_key="chat_history", return_messages=True)

        self._chain = ConversationalRetrievalChain.from_llm(self._llm, retriever=store.retriever, memory=self._memory)

    def query(self: Self, query: str) -> str:
        return self._chain(query)
