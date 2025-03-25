from fastapi import FastAPI
import gestor as g

# Creacció d'app interactiva FastAPI
app = FastAPI()

# Endpoint de root.
@app.get("/")
def read_root():
    return "Institut TIC Barcelona"

# Retorna el número total d’alumnes del centre.
@app.get("/alumnes/")
def total_alumnes():
    alumnes = g.llegir()
    total = len(alumnes)
    return total

# Retorna les dades de l’alumne amb id igual a número.
@app.get("/id/{numero}/")
def read_empleat(numero: int):
    return g.veure_alumne(numero)

# Esborra l’alumne amb id igual a número.
@app.delete("/del/{numero}/")
def esborra_empleat(numero: int):
    return g.esborra(numero)

# Afegir un alumne amb les dades proporcionades.
@app.post("/alumne/")
def crear_empleat(nom: str, cognom: str, dia: int, mes: int, any: int, email: str, feina: bool, curs: str):
    return g.afegir_alumne(nom, cognom, dia, mes, any, email, feina, curs)