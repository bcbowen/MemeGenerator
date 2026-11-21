from IngestorInterface import IngestorInterface
from TextIngestor import TextIngestor
from PdfIngestor import PdfIngestor
from CsvIngestor import CsvIngestor
from DocIngestor import DocIngestor
from QuoteModel import QuoteModel

class Ingestor(IngestorInterface): 

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        return cls in [TextIngestor, PdfIngestor, CsvIngestor, DocIngestor]

    @classmethod
    def parse(cls, path: str) -> list[QuoteModel]:
        if not Ingestor.can_ingest(cls, path): 
            raise Exception("Uningestible class!")
        #if cls is TextIngestor: 
        match str(cls): 
            case 'TextIngestor': 
                return TextIngestor.parse(cls, path)
            
