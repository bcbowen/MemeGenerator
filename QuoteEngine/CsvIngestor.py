import csv
from IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class CsvIngestor(IngestorInterface): 

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return cls is CsvIngestor

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        quotes = [] 


        with open(path, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                author = row['author']
                body = row['body']
                quotes.append(QuoteModel(body, author))
                
        return quotes