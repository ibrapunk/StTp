from typing import Dict, List
from speech_recognition import Microphone, Recognizer
import datetime




def mostrar_agenda(agenda: Dict[str, Dict[str, str]]) -> None:
    if agenda == {}:
        print("No hay puntos")
        return

    for idx, apartado in enumerate(agenda, start=1):
        print(f"{idx} - {apartado}")

    indice = int(input("Apartado a leer (indice)> "))

    if indice < 1:
        print("Indice inválido")
        return

    ap = list(agenda.keys())[indice - 1]

    sub_apartado = agenda.get(ap)
    if not apartado:
        print("Apartado inexistente")
        return

    for idx, sub in enumerate(sub_apartado.keys(), start=1):
        print(f"{idx} - {sub}")

    indice = int(input("Sub apartado a leer (indice)> "))

    if indice < 1:
        print("Índice inválido")
        return

    sup_ap = list(sub_apartado.keys())[indice - 1]

    return ap,sup_ap


def registrar_agenda() -> Dict[str, Dict[str, str]]:
    salida: Dict[str, Dict[str, str]] = {}
    
    while True:
        nombre = input("Nombre del apartado ('fin' para salir)> ")

        if nombre.lower() == "fin":
            return salida

        salida[nombre] = {}
        while True:
            subtema = input("Nombre del subtema ('fin' para salir)> ")
            if subtema.lower() == "fin":
                break
            salida[nombre][subtema] = {}


def registrar_participantes() -> List[str]:
    salida: List[str] = []
    while True:
        nombre = input("registro:Nombre del participante ('fin' para terminar)> ")
        if nombre.lower() == "fin":
            return salida
        salida.append(nombre)

def crear_entrada(apartado,subtema,participante,texto):
    entrada = {"apartado":apartado,
               "subtema":subtema,
               "participante":participante,
               "Hora":datetime.datetime.now(),
               "texto":texto,
               }
    return entrada

def reporte1(lista):
    for x in lista:
        print("Apartado: ",x["apartado"])
        print("Sub Apartado: ",x["subtema"])
        print("Participante: ",x["participante"])
        print("Hora: ",x["Hora"])
        print("Texto: ",x["texto"])
        print("\n")

def reporte2(rec,part):
    lista = []
    for x in part:
        cont = 0
        for y in rec:
            if y["participante"] == x:
                q = y["texto"].split()
                cont = cont + len(q)

        lista.append({"participante":x,"cantidad":cont})
    for x in lista:
        print("Participante: ",x["participante"])
        print("Cantidad: ",x["cantidad"])






if __name__ == "__main__":
    print("Registrando agenda")
    agenda: Dict[str, Dict[str, str]] = registrar_agenda()
    print("Agenda registrada",  "Registrando participantes")
    participantes: List[str] = registrar_participantes()
    print("Participantes registrados")
    recognizer = Recognizer()
    reconocimiento = []

    with Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=5)
        
        actual: int = 0
        while actual < 10:
            ap,sub_ap = mostrar_agenda(agenda)       

            print(*[f"-> {participante}" for participante in participantes], sep="\n")
            nombre_participante = input("Participante que hablará> ")

            try:
                participante = participantes.index(nombre_participante)
            except ValueError:
                print("Participante no existente")
                continue

            participante = participantes[participante]
            print("Di algo...")
            audio_data = recognizer.record(source, duration=5)
            texto = recognizer.recognize_google(audio_data, language="es")
            print("inicia el reconocimiento...\n")
     
            reconocimiento.append(crear_entrada(ap,sub_ap,participante,texto))

            var = input("Digite cualquier tecla para continuar con la sesion o 'Digite fin para salir'")
            if var=="fin":
                break

    print(reconocimiento)
    reporte1(reconocimiento)
    reporte2(reconocimiento,participantes)

