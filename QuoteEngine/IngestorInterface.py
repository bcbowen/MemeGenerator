from QuoteModel import QuoteModel
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    @classmethod
    @abstractmethod
    def can_ingest(cls, path: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        pass
