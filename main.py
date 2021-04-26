import pandas

def count_data_by_color(fur_color_data, color):
    return len(fur_color_data[fur_color_data['Primary Fur Color'] == color])

squirrel_data = pandas.read_csv(f'2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
fur_color_data = squirrel_data['Primary Fur Color']
counter = {}
for fur_color in fur_color_data:
    cleaned_fur_color = str(fur_color).strip()
    if cleaned_fur_color and cleaned_fur_color != 'nan':
        if counter.get(fur_color):
            counter[fur_color] += 1
        else:
            counter[fur_color] = 1
print(counter)