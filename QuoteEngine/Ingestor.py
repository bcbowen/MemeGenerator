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
        if not Ingestor.can_ingest(path): 
            raise Exception("Uningestible class!")

        match str(cls): 
            case 'TextIngestor': 
                return TextIngestor.parse(path)
            case 'PdfIngestor': 
                            return PdfIngestor.parse(path)
            case 'DocIngestor': 
                            return DocIngestor.parse(path)
            case 'CsvIngestor': 
                            return CsvIngestor.parse(path)
        raise Exception("Unrecognized cls: " + str(cls))
