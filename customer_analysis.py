import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')

df.head() # to see the first 5 rows
df.info() # to understand the content of the columns
df.describe(include='all') # statistic of all the columns

df.isnull().sum() # looking to all the null value

# if the value is null, we substitute it with the median value based on the category group
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())

# reassigning new names without spaces and capital letters to the columns
df.columns = df.columns.str.lower() 
df.columns = df.columns.str.replace(" ", "_")
df = df.rename(columns={"purchase_amount_(usd)" : "purchase_amount"})
print(df.columns)

# creating a new column age_group 
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df["age_group"] = pd.qcut(df['age'], q=4, labels= labels) #4 age category divided in 4 range
print(df[["age", "age_group"]].head(10))

# creating column purchase_frequency_days
# transforming the already had frequency into a numeric frequency
frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
print(df[["purchase_frequency_days", "frequency_of_purchases"]].head(10))

# checking if the discount_applied and promo_code_used columns are the same (REDUNDANCY)
print((df["discount_applied"] == df["promo_code_used"]).all()) #true
df = df.drop("promo_code_used", axis=1)
print(df.columns)

new_file = df.to_csv("new_customer_shopping_behavior.csv", index=False)