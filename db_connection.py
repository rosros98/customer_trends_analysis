# Connect to PostgreSQL
from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv('new_customer_shopping_behavior.csv')

username = "postgres"
password = "sector17!"
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Load dataframe into postgresql
table_name = "customer"
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loadad into table '{table_name} in database '{database}.")