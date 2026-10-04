import pandas as pd
import seaborn as sns
import numpy as np

# Load the dataset
nobel = pd.read_csv('data/nobel.csv')

# 1. Most common gender and birth country
top_gender = nobel['sex'].value_counts().index[0]
top_country = nobel['birth_country'].value_counts().index[0]

# 2. Decade with highest ratio of US-born winners
nobel['us_born_winner'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
prop_usa_winners = nobel.groupby('decade', as_index=False)['us_born_winner'].mean()

# Explicitly cast to Python int to satisfy DataCamp's type check
max_decade_usa = int(prop_usa_winners.sort_values('us_born_winner', ascending=False).iloc[0]['decade'])

# 3. Decade and category combination with highest proportion of female laureates
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(['decade', 'category'], as_index=False)['female_winner'].mean()
max_female_row = prop_female_winners.sort_values('female_winner', ascending=False).iloc[0]
max_female_dict = {int(max_female_row['decade']): max_female_row['category']}

# 4. First woman to receive a Nobel Prize
female_nobel = nobel[nobel['female_winner']]
first_woman = female_nobel.sort_values('year').iloc[0]
first_woman_name = first_woman['full_name']
first_woman_category = first_woman['category']

# 5. Repeat winners
counts = nobel['full_name'].value_counts()
repeat_list = list(counts[counts >= 2].index)
