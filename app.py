from fastapi import FastAPI
import uvicorn
from operaciones.data_base.database import conectar_base_datos
from operaciones.data_base.consulta_clientes import consultar_clientes


app = FastAPI(title="API sencilla")

@app.get("/")
def root():
    return {"message": "Hola mundo desde FastAPI"}

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    conexion, cursor = conectar_base_datos(nombre_bd="datos.db")
    cliente = consultar_clientes(cursor, user_id)
    conexion.close()
    return {"user":cliente}

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
