'''to extract data'''


class DataExtractor:
    '''DataExtractor class'''
    data_in_file = []

    def extract(self, file):
        '''to extract data'''
        with open(file, 'r', encoding='utf-8') as datfile:
            data_in_file = [data.split() for data in datfile]
        for i, _ in enumerate(data_in_file):
            if '-' in data_in_file[i]:
                index_value = data_in_file[i].index('-')
                del data_in_file[i][index_value]
        for i, _ in enumerate(data_in_file):
            if len(data_in_file[i]) == 1 or len(data_in_file[i]) == 0:
                del data_in_file[i]

        return data_in_file
