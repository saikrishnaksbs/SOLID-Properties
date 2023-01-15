def calculate(climate_data):
    '''To calculate'''
    columns_names = climate_data[0]
    print(columns_names)
    mxt_index = climate_data[0].index('MxT')
    mnt_index = climate_data[0].index('MnT')
    day_index = climate_data[0].index('Dy')
    smallest_temperature_spread = 10000
    day_with_low_spread = 1000
    for index, _ in enumerate(climate_data):
        if index != 0 and index != 1:
            mxt_data = climate_data[index][mxt_index]
            mnt_data = climate_data[index][mnt_index]
            day = climate_data[index][day_index]
            if len(mxt_data) > 2:
                mxt_data = mxt_data[:2]
            if len(mnt_data) > 2:
                mnt_data = mnt_data[:2]
            day_temp_difference = int(mxt_data)-int(mnt_data)
            if day_temp_difference < smallest_temperature_spread:
                smallest_temperature_spread = day_temp_difference
                day_with_low_spread = day

    print(day_with_low_spread)
    return day_with_low_spread


with open("weather.dat", 'r', encoding='utf-8') as datFile:
    weather_data = [data.split() for data in datFile]

print(weather_data)
lowest_temp_spread = calculate(weather_data)
print(lowest_temp_spread)
