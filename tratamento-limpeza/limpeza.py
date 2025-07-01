from datetime import datetime
import pandas as pd
import os

caminho_arquivo = '../online_retail_II.xlsx'  

if not os.path.exists(caminho_arquivo):
    raise FileNotFoundError(f"Not found: {caminho_arquivo}")

df = pd.read_excel(caminho_arquivo)

# Criação de colunas
df['datetime'] = pd.to_datetime(df['InvoiceDate'], format='%d/%m/%Y %H:%M')

df['day'] = df['datetime'].dt.day_name()

# Classificação da refeição por horário
def classification_meal(hour):
    if 5 <= hour < 11:
        return 'breakfast'
    elif 11 <= hour < 15:
        return 'lunch'
    elif 18 <= hour < 22:
        return 'dinner'
    else:
        return 'other'

df['meal_day'] = df['datetime'].dt.hour.apply(classification_meal)
df.rename(columns={'Description': 'name'}, inplace=True)
df.drop(['Invoice', 'StockCode', 'Quantity', 'InvoiceDate', 'Price', 'Customer ID', 'Country']
, axis=1, inplace=True)


df.to_csv('../clean_data.csv', index=False, sep=';')