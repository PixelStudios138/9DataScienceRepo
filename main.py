import pandas as pd

df = pd.read_csv("athlete_events.csv")

print(df.head())
print(df.columns)

print(df['Sport'].value_counts().head())
print(df['Sex'].value_counts())

print(df.describe())

print(df['NOC'].nunique())
print(df['NOC'].unique())

# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print(female_athletes.head())

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print(older_athletes[['Name', 'Age', 'Sport']].head())

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
print(combo_filter[['Name', 'Age', 'Sport']].head())

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
print(basketball_males.head())

# Australian swimmers
australian_swimmers = df[((df['Team'] == 'Australia') & (df['Sport'] == "Swimming"))]
print(australian_swimmers.head())

# Sort by age
sorted_by_age = df.sort_values(by='Age', ascending=False)
print(sorted_by_age[['Name', 'Age', 'Sport']].head())

# Sort by weight
sorted_by_weight = df.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head())

# Sort by height and weight
sorted_by_weight2 = df.sort_values(by='Weight', ascending=False)
sorted_by_height = sorted_by_weight2.sort_values(by='Height', ascending=False)
print(sorted_by_height[['Name', 'Height', 'Weight', 'Sport']].head(10))

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count medals per team
medals_by_team = df[df['Medal'].notnull()].groupby('Team')['Medal'].count()
print(medals_by_team.sort_values(ascending=False).head())

# Count participants in each sport
sport_female_counts = female_athletes['Sport'].value_counts()
print(sport_female_counts.head())

# Average height per sport
avg_height = df.groupby('Sport')['Height'].mean().sort_values(ascending=False)
print(avg_height.head())

# Median age by year
median_age_by_year = df.groupby('Year')['Age'].median()
print(median_age_by_year.tail())

# Average weight per sex and sport
male_athletes = df[df['Sex'] == 'M']
avg_male_weight = male_athletes.groupby('Sport')['Weight'].mean().sort_values(ascending=False)
avg_female_weight = female_athletes.groupby('Sport')['Weight'].mean().sort_values(ascending=False)
print(avg_male_weight.head())
print(avg_female_weight.head())

# Filter gymnasts and save to new CSV
gymnasts = df[df['Sport'] == 'Gymnastics']
gymnasts.to_csv('gymnastics_athletes.csv', index=False)

# Filter under 18 and save to new CSV
kids = df[df['Age'] < 18]
kids.to_csv('child_athletes.csv', index=False)

# Filter gold medalists and save to new CSV
gold_medalists = df[df['Medal'] == 'Gold']
gold_medalists.to_csv('gold_medal_athletes.csv', index=False)

# Count missing values in each column
print(df.isnull().sum())

# Drop rows missing both height and weight
df_cleaned = df.dropna(subset=['Height', 'Weight'])
print(df_cleaned.shape)

# Fill missing medals with 'None'
df_cleaned['Medal'] = df_cleaned['Medal'].fillna('None')

# Fill missing ages with average age
avg_age = df_cleaned['Age'].mean()
df_cleaned['Age'] = df_cleaned['Age'].fillna(avg_age)

# Fill missing weights with median weights
avg_weight = df_cleaned['Weight'].median()
df_cleaned['Weight'] = df_cleaned['Weight'].fillna(avg_weight)

# Unique values in 'Sex' and 'Medal'
print(df_cleaned['Sex'].unique())
print(df_cleaned['Medal'].unique())

# Check again for missing values
print(df_cleaned.isnull().sum())

# Get stats after cleaning
print(df_cleaned.describe())

# Save your cleaned version
df_cleaned.to_csv("athlete_events_cleaned.csv", index=False)
