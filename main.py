from fastapi import FastAPI, Request
from pydantic import BaseModel
import random

app = FastAPI()

bomba_estado = 0  # 0 = desligada, 1 = ligada

class BombaCommand(BaseModel):
    estado: int  # 0 ou 1

@app.post("/bomba")
def controlar_bomba(cmd: BombaCommand):
    global bomba_estado
    if cmd.estado in [0, 1]:
        bomba_estado = cmd.estado
        return {"mensagem": f"Bomba {'ligada' if bomba_estado else 'desligada'}"}
    return {"erro": "Estado inválido. Use 0 ou 1."}

@app.get("/dados")
def obter_dados():
    temperatura = round(random.uniform(20.0, 35.0), 2)
    umidade = round(random.uniform(40.0, 80.0), 2)
    sensor_umidsolo = round(random.uniform(0, 100.0), 5)
    pH= round(random.uniform(0, 14), 1)
    return {
        "temperatura": temperatura,
        "umidade": umidade,
        "bomba": bomba_estado,
       “sensor_umidsolo”: sensor_umidsolo,
       “pH”:pH
    }
