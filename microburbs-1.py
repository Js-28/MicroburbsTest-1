import pandas as pd


cities = ['Sydney', 'Melbourne', 'Brisbane', 'Adelaide', 'Perth', 'Hobart', 'Canberra']

seasons = ['Summer', 'Autumn', 'Winter', 'Spring']


weather_descriptions = {
    'Sydney': ['Hot and humid', 'Mild and pleasant', 'Cool and rainy', 'Warm and sunny'],
    'Melbourne': ['Hot and dry', 'Cool and windy', 'Cold and wet', 'Mild and sunny'],
    'Brisbane': ['Hot and humid', 'Warm and pleasant', 'Cool and dry', 'Warm and sunny'],
    'Adelaide': ['Hot and dry', 'Cool and windy', 'Cold and wet', 'Mild and sunny'],
    'Perth': ['Hot and dry', 'Mild and pleasant', 'Cool and dry', 'Warm and sunny'],
    'Hobart': ['Cool and rainy', 'Cold and windy', 'Cold and wet', 'Cool and sunny'],
    'Canberra': ['Hot and dry', 'Cool and pleasant', 'Cold and frosty', 'Mild and sunny']
}

weather_data = {city: [] for city in cities}


for season in seasons:
    for city in cities:
        weather_description = weather_descriptions.get(city, ['N/A'])[seasons.index(season)]
        weather_data[city].append(weather_description)


df = pd.DataFrame(weather_data, index=seasons)


df.to_csv('australian_weather.csv')

print("CSV file 'australian_weather.csv' has been created.")
