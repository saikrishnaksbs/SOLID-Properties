'''to analyze'''


class DataAnalyzer:
    '''DataAnalyzer class'''

    def analyzer(self, file_data, field1, field2, field3):
        '''to analyze'''

        index1 = file_data[0].index(field1)
        index2 = file_data[0].index(field2)
        index3 = file_data[0].index(field3)
        min_difference = 10000
        final_result = ''
        for index, _ in enumerate(file_data):
            if index != 0:
                data1_field = file_data[index][index1]
                data2_field = file_data[index][index2]
                req_field = file_data[index][index3]
                if len(data1_field) > 2:
                    data1_field = data1_field[:2]
                if len(data2_field) > 2:
                    data2_field = data2_field[:2]
                difference = abs(int(data1_field)-int(data2_field))
                if difference < min_difference:
                    min_difference = difference
                    final_result = req_field

        return final_result
