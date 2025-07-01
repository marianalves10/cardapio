import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

model_path = '../modelo-encoder/model_meal.h5'
X_test_path = '../modelo-encoder/X_test.npy'
y_test_path = '../modelo-encoder/y_test.npy'
label_classes_path = '../modelo-encoder/label_encoder_classes.npy'

model = load_model(model_path)
X_test = np.load(X_test_path)
y_test = np.load(y_test_path)
label_classes = np.load(label_classes_path, allow_pickle=True)

le = LabelEncoder()
le.classes_ = label_classes

y_pred_probs = model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

acc = accuracy_score(y_test, y_pred)
print(f"Acurácia no conjunto de teste: {acc:.2f}")

print("Exemplos de previsão:")
for i in range(5):
    real = le.inverse_transform([y_test[i]])[0]
    predicted = le.inverse_transform([y_pred[i]])[0]
    print(f"{i+1}. Real: {real} | Previsto: {predicted}")

for i, prato in enumerate(le.classes_):
    print(f"{i}: {prato}")
