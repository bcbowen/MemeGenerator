from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class TextIngestor(IngestorInterface): 

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return cls is TextIngestor

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        quotes = [] 

        with open(path, 'r', encoding='utf-8-sig') as file: 
            for line in file.readlines():
                quote, name = line.split('-') 
                quotes.append(QuoteModel(quote.strip(), name.strip()))
        return quotes