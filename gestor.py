# Importem les llibreries necessaries per al projecte.
import json # json -> per apuntar i llegir el fitxer on es guarden les dades
import os # os -> per netejar la pantalla

### FUNCIONS ############################################################

# Llegir document alumnes.json, el transforma en "dict" i el retorna.
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
def mostra_tots(alumnes: list[dict]):
    for alumne in alumnes:
        print(alumne["id"], alumne["nom"], alumne["cognom"])

# Crea un dict d'alumne amb les dades que s'han passat. I l'afageix al fitxer
def afegir_alumne(alumnes: list[dict], nom: str, cognom: str, dia: int, mes: int, any: int, email: str, feina: bool, curs: str):
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

# Retorna tots els detalls d'un alumne segons l'id.
def veure_alumne(alumnes: list[dict], id: int):
    for alumne in alumnes:
        if alumne["id"] == id:
            return alumne
    return "L'alumne amb id: {} no existeix".format(id)

# Esborra un alumne segons l'id
def esborra(alumnes: list[dict], id: int):
    for alumne in alumnes:
        if alumne["id"] == id:
            i = alumnes.index(alumne)
            alumnes.pop(i)
            desar(alumnes)
            return "Alumne esborrat"
    return "L'alumne amb id: {} no existeix".format(id)

### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla.
#
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    # Netejem la pantalla
    os.system('clear')

    # Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")

    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    # i retornem l'opció escollida per l'usuari
    return input()

### Programa ################################################

# Llista d'Alumnes
alumnes = []

# Fins a l'infinit (i més enllà)
while True:

    # Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('clear')
            print("Mostrar alumnes")
            print("-------------------------------")

            mostra_tots(alumnes)

            input()

        # Afegir alumne ##################################
        case "2":
            os.system('clear')
            print("Afegir alumne")
            print("-------------------------------")
            print("Afegeix les dades de l'alumne")

            print(afegir_alumne(alumnes,
                input("nom: "),
                input("cognom: "),
                int(input("dia: ")),
                int(input("mes: ")),
                int(input("any: ")),
                input("email: "),
                bool(input("feina: ")),
                input("curs: ")
            ))

            input()

        # Veure alumne ##################################
        case "3":
            os.system('clear')
            print("Veure alumne")
            print("-------------------------------")
            print("Quin alumne vols veure?")

            print(veure_alumne(alumnes,
                int(input("id: "))
            ))

            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('clear')
            print("Esborrar alumne")
            print("-------------------------------")
            print("Quin alumne vols eliminar?")

            print(esborra(alumnes,
                int(input("id: "))
            ))

            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('clear')
            print("Desar a fitxer")
            print("-------------------------------")

            print(desar(
                alumnes
            ))

            input()

        # Llegir fitxer ##################################
        case "6":
            os.system('clear')
            print("Llegir fitxer")
            print("-------------------------------")

            alumnes = llegir()
            print("S'ha llegit el fitxer")

            input()

        # Sortir ##################################
        case "0":
            os.system('clear')
            print("Adeu!")

            # Trenquem el bucle infinit
            break

        # Qualsevol altra cosa #####################
        case _:
            print("\nOpció incorrecta\a")
            input()