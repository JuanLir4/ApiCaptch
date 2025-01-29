
from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from PIL import Image
from keras.models import load_model


model = load_model("./modelos/redeneural.h5")
app = FastAPI()

#preciso carregar o modelo

@app.get("/")
async def root():
    return {"message": "Hello World"}


def fileToNumpy(file: File) -> np:
    #o atributo file de file cria um arquivo temporario do tipo SpooledTemporaryFile, depois a lib usar open para carregar esse arquivo em bytes
    image = Image.open(file.file)
    #convertendo para escala de cinza
    image = image.convert("L")
    #redimensionando imagem
    image = image.resize((200, 50))
    
    
    imageNumpy = np.array(image)
    
    #normalizando:
    imageNumpy = imageNumpy / 255.0
    
    #ajustando dimensoes(acho q da no msm de usar expand):
    imageNumpy = np.reshape(imageNumpy, (50, 200, 1))
    
    imageNumpy = np.expand_dims(imageNumpy, axis=0)
    
    
    return imageNumpy
    


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    
    #file para array numpy
    imagem = fileToNumpy(file)
    resultado = model.predict(imagem)
    #remove a dimensao extra
    resultado = np.vstack(resultado)
    
    resultado = np.argmax(resultado, axis=1)
    
    resultado = resultado.tolist()
    
    return {
        'resposta': resultado
        
        }
    
    #permissao pro front rodar
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  #
    allow_credentials=True,
    allow_methods=["http://localhost:3000"],
    allow_headers=["http://localhost:3000"],
)



#pra evitar que eu use uvicorn main:app -- reload
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000)
    
    

#testar post: terminal linux
# curl -X POST "http://localhost:8000/uploadfile/" -F "file=@./CaptchaDataSet/test-images/test-images/image_test_1.png"