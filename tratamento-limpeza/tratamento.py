import pandas as pd
import numpy as np
import os

# Leitura do csv
caminho_arquivo = '../clean_data.csv'  

if not os.path.exists(caminho_arquivo):
    raise FileNotFoundError(f"Not found: {caminho_arquivo}")

df = pd.read_csv(caminho_arquivo, sep=';')

# Tira espaço do fim e inicio, e coloca minusculo
df['name'] = df['name'].str.strip().str.lower() 
counts = df['name'].value_counts()

rare_names = counts[counts == 1].index

# Agrupa por linhas que tem só 1 aparição
df['name'] = df['name'].apply(lambda x: 'others' if x in rare_names else x) 
df.to_csv('../clean_data.csv', index=False, sep=';')