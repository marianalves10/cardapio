from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model
import uvicorn



class MealSequence(BaseModel):
    sequence: list[int]  

app = FastAPI()

model_path = '../modelo-encoder/model_meal.h5'
classes_path = '../modelo-encoder/label_encoder_classes.npy'



model = load_model(model_path)
classes = np.load(classes_path, allow_pickle=True)

window_size = 4  

@app.get("/")
async def root():
    return {"message": "API de previsão de prato - Envie uma sequência para prever o próximo prato."}

@app.post("/predict/")
async def predict_next_meal(data: MealSequence):
    seq = data.sequence
    if len(seq) != window_size:
        raise HTTPException(status_code=400, detail=f"Sequência deve ter exatamente {window_size} elementos.")

    
    X_input = np.array(seq).reshape(1, window_size)

    
    preds = model.predict(X_input)
    pred_index = np.argmax(preds, axis=1)[0]
    pred_class = classes[pred_index]

    return {
        "predicted_class_index": int(pred_index),
        "predicted_class_name": str(pred_class)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


#uvicorn predict:app --reload
