from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class DocIngestor(IngestorInterface): 

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return cls is DocIngestor

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        quotes = [] 

        #with open(path, 'r') as file: 
        #    for line in file.readlines():
        #        quote, name = line.split('-') 
        #        quotes.append(QuoteModel(quote.strip(), name.strip()))
        return quotes