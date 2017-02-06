import pandas as pd

df = pd.read_csv('parsed_ingredients.csv')

pd.DataFrame(list(set(df['ingredient']))).to_csv('ingredient_list.csv')



