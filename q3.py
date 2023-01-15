class Calculator:
    '''Calculator class'''

    def __init__(self):
        self.ext = self.DataExtractor()
        self.ana = self.DataAnalyzer()

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

    # create a 2nd Inner class
    class DataAnalyzer:
        '''DataAnalyzer class'''

        def analyzer(self, file_data, field1, field2, field3):
            '''to analyze'''
            columns_names = file_data[0]
            print(columns_names)
            mxt_index = file_data[0].index(field1)
            mnt_index = file_data[0].index(field2)
            day_index = file_data[0].index(field3)
            smallest_temperature_spread = 10000
            day_with_low_spread = ''
            for index, _ in enumerate(file_data):
                if index != 0:
                    mxt_data = file_data[index][mxt_index]
                    mnt_data = file_data[index][mnt_index]
                    day = file_data[index][day_index]
                    if len(mxt_data) > 2:
                        mxt_data = mxt_data[:2]
                    if len(mnt_data) > 2:
                        mnt_data = mnt_data[:2]
                    day_temp_difference = abs(int(mxt_data)-int(mnt_data))
                    if day_temp_difference < smallest_temperature_spread:
                        smallest_temperature_spread = day_temp_difference
                        day_with_low_spread = day

            return day_with_low_spread


main_class = Calculator()

# create a object
# of 1st inner class
d1 = main_class.ext
extracted_data1 = d1.extract("weather.dat")

d3 = main_class.ana
final_result1 = d3.analyzer(extracted_data1, 'MxT', 'MnT', 'Dy')
print(final_result1)


d2 = main_class.ext
extracted_data2 = d2.extract("football.dat")

d4 = main_class.ana
final_result2 = d4.analyzer(extracted_data2, 'A', 'Pts', 'P')
print(final_result2)
