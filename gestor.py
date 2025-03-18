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

# Desa el parametre dic al fitxer, transformant-lo en json.
def desar(dic: list[dict]):
    fitxer = open("alumnes.json", "wt")
    s = json.dumps(dic, indent=4)
    fitxer.write(s)
    fitxer.close()
    return "Desat correctament"

# Mostra l'id, el nom i el cognom de tots els alumnes.
def mostra_tots():
    alumnes = llegir()
    for alumne in alumnes:
        print(alumne["id"], alumne["nom"], alumne["cognom"])

# Afegeix un alumne.
def afegir_alumne(nom: str, cognom: str, dia: int, mes: int, any: int, email: str, feina: bool, curs: str):
    alumnes = llegir()
    id = alumnes[len(alumnes) - 1]["id"] + 1
    alumne = {
        "id": id,
        "nom": nom,
        "cognom": cognom,
        "data": {
            "dia": dia,
            "mes": mes,
            "any": any
        },
        "email": email,
        "feina": feina,
        "curs": curs
    }
    alumnes.append(alumne)
    desar(alumnes)
    return "Alumne afegit"

# Mostra tots els detalls d'un alumne segons l'id.
def veure_alumne(id: int):
    alumnes = llegir()
    for alumne in alumnes:
        if alumne["id"] == id:
            result = json.dumps(alumne, indent=4)
            return result
    return "L'alumne amb id: {} no existeix".format(id)

# Esborra un alumne segons l'id
def esborra(id: int):
    alumnes = llegir()
    for alumne in alumnes:
        if alumne["id"] == id:
            i = alumnes.index(alumne)
            alumnes.pop(i)
            desar(alumnes)
            return "Alumne esborrat"
    return "L'alumne amb id: {} no existeix".format(id)