import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\91705\Desktop\Amazon-Sales-Analysis\Data\Amazon Sale Report.csv")


# print(df.columns)       
# print(df.info()) 

#print(df.head)
df=df.drop(columns=['fulfilled-by','New','PendingS','Unnamed: 21'])

df['currency']=df['currency'].fillna('INR')
df['Date'] = pd.to_datetime(df['Date'])
df['ship-postal-code'] = df['ship-postal-code'].astype('Int64').astype(str)
df = df.dropna()
print(df.isnull().sum())
print(df.shape)
print(df.dtypes)


df.to_csv(r"C:\Users\91705\Desktop\Amazon-Sales-Analysis\Data\Amazon_Sale_Report_Cleaned.csv", index=False)

