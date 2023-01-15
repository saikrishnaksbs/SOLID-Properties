def calculate(fball_data):
    '''To calculate'''
    columns_names = [fball_data[0]]
    print(columns_names)
    f_index = columns_names[0].index('F')+1
    a_index = columns_names[0].index('A')+1
    team_index = columns_names[0].index('Team')+1
    smallest_difference = 10000
    team = ''
    print(f_index, a_index)
    for index, _ in enumerate(fball_data):
        if index != 0 and index != 1:
            f_data = fball_data[index][f_index]
            a_data = fball_data[index][a_index]
            team_data = fball_data[index][team_index]
            f_and_a_difference = abs(int(f_data)-int(a_data))
            if f_and_a_difference < smallest_difference:
                smallest_difference = f_and_a_difference
                team = team_data
    print(team)
    return team


with open("football.dat", 'r', encoding='utf-8') as datFile:
    football_data = [data.split() for data in datFile]
for i, _ in enumerate(football_data):
    if '-' in football_data[i]:
        index_value = football_data[i].index('-')
        del football_data[i][index_value]

for i, _ in enumerate(football_data):
    if len(football_data[i]) == 1:
        del football_data[i]


print(football_data)
team_name = calculate(football_data)
print(team_name)
