import unittest
from CsvIngestor import CsvIngestor
from PdfIngestor import PdfIngestor
import csv
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2] 

class test_csv_ingestor(unittest.TestCase): 


    def setUp(self):
        self.data_root = PROJECT_ROOT / '_data'
        self.csv_file = self.data_root / 'DogQuotes/DogQuotesCSV.csv'

    def test_DataPathFound(self):
        self.assertTrue(self.data_root.exists()) 

    def test_CsvFileFound(self): 
        self.assertTrue(self.csv_file.exists())

    def test_TextIngestorReadsExpectedNumberOfRows(self): 
        if self.csv_file.exists(): 
            ci = CsvIngestor()
            result = ci.parse(str(self.csv_file))
            self.assertEqual(len(result), 2)
        else: 
            self.skipTest("Unable to find text file")
    
    def test_TextIngestorParsesFileCorrectly(self): 
        if self.csv_file.exists(): 
            ci = CsvIngestor()
            result = ci.parse(str(self.csv_file))
            if len(result) == 2: 
                self.assertEqual(len(result), 2)
                """
                Chase the mailman,Skittle
                "When in doubt, go shoe-shopping",Mr. Paws
                """
                for quote in result: 
                    self.assertTrue(quote.author in ['Skittle', 'Mr. Paws'])
                    match quote.author: 
                        case 'Skittle': 
                            self.assertEqual(quote.body, 'Chase the mailman')
                        case 'Mr. Paws':
                            self.assertEqual(quote.body, 'When in doubt, go shoe-shopping') 
            else: 
                self.skipTest("Unable to run this test, the rows did not load correctly")
        else: 
            self.skipTest("Unable to find text file")