import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from db_connection import collection


data = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
sns.histplot(df["Asian Men"], bins=30, kde=True, color="blue", label="Erkek")
sns.histplot(df["Asian Women"], bins=30, kde=True, color="red", label="Kadın")
plt.title("Kadın ve Erkek Çalışanların Maaş Dağılımı (Asian)")
plt.xlabel("Maaş")
plt.ylabel("Frekans")
plt.legend()
plt.show()


plt.figure(figsize=(10, 5))
sns.histplot(df["Total Men"], bins=30, kde=True, color="blue", label="Erkek")
sns.histplot(df["Total Women"], bins=30, kde=True, color="red", label="Kadın")
plt.title("Kadın ve Erkek Çalışanların Maaş Dağılımı (Total)")
plt.xlabel("Maaş")
plt.ylabel("Frekans")
plt.legend()
plt.show()


plt.figure(figsize=(10, 5))
sns.histplot(df["Asian Men"], bins=30, kde=True, color="blue", label="Erkek")
sns.histplot(df["Asian Women"], bins=30, kde=True, color="red", label="Kadın")
plt.axvline(df["Asian Men"].mean(), color='blue', linestyle='--', label="Erkek Ortalaması")
plt.axvline(df["Asian Women"].mean(), color='red', linestyle='--', label="Kadın Ortalaması")
plt.title("Kadın ve Erkek Çalışanların Maaş Dağılımı (Ortalama ile)")
plt.xlabel("Maaş")
plt.ylabel("Frekans")
plt.legend()
plt.show()


df["Normalized Asian Men"] = (df["Asian Men"] - df["Asian Men"].min()) / (df["Asian Men"].max() - df["Asian Men"].min())
df["Normalized Asian Women"] = (df["Asian Women"] - df["Asian Women"].min()) / (df["Asian Women"].max() - df["Asian Women"].min())

plt.figure(figsize=(10, 5))
sns.histplot(df["Normalized Asian Men"], bins=30, kde=True, color="blue", label="Erkek")
sns.histplot(df["Normalized Asian Women"], bins=30, kde=True, color="red", label="Kadın")
plt.title("Kadın ve Erkek Çalışanların Normalize Maaş Dağılımı")
plt.xlabel("Normalize Maaş")
plt.ylabel("Frekans")
plt.legend()
plt.show()
