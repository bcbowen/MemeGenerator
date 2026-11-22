import unittest
from TextIngestor import TextIngestor
from PdfIngestor import PdfIngestor
#import os
import pathlib

PROJECT_ROOT = pathlib.Path(__file__).resolve().parents[2] 

class test_text_ingestor(unittest.TestCase): 


    def setUp(self):
        self.data_root = PROJECT_ROOT / '_data'
        self.text_file = self.data_root / 'DogQuotes/DogQuotesTXT.txt'

    def test_DataPathFound(self):
        self.assertTrue(self.data_root.exists()) 

    def test_TextFileFound(self): 
        self.assertTrue(self.text_file.exists())

    def test_TextIngestorReadsExpectedNumberOfRows(self): 
        if self.text_file.exists(): 
            t = TextIngestor()
            result = t.parse(str(self.text_file))
            self.assertEqual(len(result), 2)
        else: 
            self.skipTest("Unable to find text file")
    
    def test_TextIngestorParsesFileCorrectly(self): 
        if self.text_file.exists(): 
            t = TextIngestor()
            result = t.parse(str(self.text_file))
            if len(result) == 2: 
                self.assertEqual(len(result), 2)
                """
                To bork or not to bork - Bork
                He who smelt it... - Stinky
                """
                for quote in result: 
                    self.assertTrue(quote.author in ['Bork', 'Stinky'])
                    match quote.author: 
                        case 'Bork': 
                            self.assertEqual(quote.body, 'To bork or not to bork')
                        case 'Stinky':
                            self.assertEqual(quote.body, 'He who smelt it...') 
            else: 
                self.skipTest("Unable to run this test, the rows did not load correctly")
        else: 
            self.skipTest("Unable to find text file")
     