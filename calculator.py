'''for analyzing and extracting'''

from dataanalyzer import DataAnalyzer
from dataextractor import DataExtractor


class Calculator:
    '''Calculator class'''

    def __init__(self):

        self.data_extractor = DataExtractor()
        self.data_analyzer = DataAnalyzer()
        self.extracted_data = []

    def exctract(self, filename):
        '''for extracting'''
        self.extracted_data = self.data_extractor.extract(filename)

    def analyze(self, field1, field2, field3):
        '''for analyzing'''
        final_result1 = self.data_analyzer.analyzer(self.extracted_data,
                                                    field1, field2, field3)
        print(final_result1)
