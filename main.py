import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from irisModel import IrisMachineLearning, IrisSpecies

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):\d+",
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

model = IrisMachineLearning()
@app.get("/")
async def root():
    return {"message": "Hello, this is iris classifier 2025/3/10"}

@app.get("/predict")
async def predict():
    pred = model.predict_species(5.0, 3.4, 1.4, 0.2)
    return {"prediction": pred}

@app.post("/predict")
async def predict_species(iris: IrisSpecies):
    pred = model.predict_species(iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width)
    return {"prediction": pred}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
