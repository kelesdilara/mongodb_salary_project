import pandas as pd
from db_connection import collection

df = pd.read_csv("salary_bras.csv")


collection.insert_many(df.to_dict(orient="records"))

print("CSV verisi başarıyla MongoDB'ye yüklendi!")
