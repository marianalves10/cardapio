
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import LSTM
import os

caminho_arquivo = '../clean_data.csv'

if not os.path.exists(caminho_arquivo):
    raise FileNotFoundError(f"Not found: {caminho_arquivo}")
df = pd.read_csv(caminho_arquivo, sep=';')

le = LabelEncoder()
df['prato_encoded'] = le.fit_transform(df['name'])

window_size = 4
X, y = [], []

for i in range(len(df) - window_size):
    seq_x = df['prato_encoded'].iloc[i:i+window_size].values
    seq_y = df['prato_encoded'].iloc[i+window_size]
    X.append(seq_x)
    y.append(seq_y)

X = np.array(X)
y = np.array(y)

# Crie o modelo LSTM
model = Sequential()
model.add(Embedding(input_dim=len(le.classes_), output_dim=50, input_length=window_size))
model.add(LSTM(64))
model.add(Dense(len(le.classes_), activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

model.fit(X_train, y_train, epochs=20, batch_size=16)

# Salva as informações
model.save('../modelo-encoder/model_meal.h5')
np.save('../modelo-encoder/label_encoder_classes.npy', le.classes_)

np.save('../modelo-encoder/X_test.npy', X_test)
np.save('../modelo-encoder/y_test.npy', y_test)
