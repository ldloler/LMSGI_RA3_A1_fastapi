# Importem les llibreries necessaries per al projecte.
from pydantic import BaseModel
import json

# Objecte Data, guardem dia, mes i any
class Data(BaseModel):
    dia: int
    mes: int
    any: int

# Objecte Alumne, amb els atributs que volem guardar.
class Alumne(BaseModel):
    id: int
    nom: str
    cognom: str
    data: Data # Guardem un objecte Data.
    email: str
    feina: bool
    curs: str

# Llegir document alumnes.json, es transforma en "dict" i el retorna.
def llegir():
    fitxer = open("alumnes.json", "rt")
    s = fitxer.read()
    dic = json.loads(s)
    fitxer.close()
    return dic

# Desa el parametre dic al fitxer, transformantse en json.
def desar(dic: dict):
    fitxer = open("alumnes.json", "wt")
    s = json.dumps(dic)
    fitxer.write(s)
    fitxer.close()
    return "Desat correctament"