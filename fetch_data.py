import pandas as pd
from db_connection import collection


data = list(collection.find({}, {"_id": 0}))


df = pd.DataFrame(data)


print(df.head())
print("Veri setindeki sütunlar:", df.columns)
