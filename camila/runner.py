from pathlib import Path
from typing import Self

from camila.chain import Chain
from camila.loader import Loader
from camila.processing import CharacterProcessor, MarkdownProcessor, Processor
from camila.settings import Settings
from camila.store import Store


class Runner:
    def __init__(self: Self, settings: Settings) -> None:
        self._settings = settings

        self._loader = Loader()
        self._store = Store(settings=self._settings)
        self._chain = Chain(settings=self._settings, store=self._store)

        self._processors: list[type[Processor]] = [
            MarkdownProcessor,
            CharacterProcessor,
        ]

    def load(self: Self, path: Path | str) -> None:
        if Path(path).is_dir():
            self._loader.load_directory(path=path, glob="**/*.md")
        else:
            self._loader.load_file(path=path)

        documents = []

        for processor_cls in self._processors:
            processor = processor_cls(self._loader.documents)
            documents.extend(processor.process())

        self._store.add_documents(self._loader.documents)

    def run_query(self: Self, query: str) -> str:
        return self._chain.query(query)
