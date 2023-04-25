import speech_recognition as sr
from collections import defaultdict

# Función para registrar los puntos de la agenda
def registrar_punto_agenda():
    puntos_agenda = []
    while True:
        punto = input("Ingrese un punto de la agenda (o escriba 'fin' para terminar): ")
        if punto == "fin":
            break
        else:
            puntos_agenda.append(punto)
    return puntos_agenda

# Función para registrar la lista de participantes
def registrar_participantes():
    participantes = []
    while True:
        participante = input("Ingrese el nombre de un participante (o escriba 'fin' para terminar): ")
        if participante == "fin":
            break
        else:
            participantes.append(participante)
    return participantes

# Función para transcribir la participación de cada miembro
def transcribir_participacion(punto, participante):
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print(f"{participante}, por favor hable sobre el punto de agenda '{punto}'")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Transcribiendo...")

    try:
        participacion = r.recognize_google(audio, language="es-ES")
        print(f"{participante} ha dicho: {participacion}")
        return participacion
    except:
        print(f"No se ha podido transcribir la participación de {participante}")
        return ""

# Función para generar el informe de la sesión
def generar_informe(participantes, puntos_agenda, transcripciones):
    print("Informe de la sesión:\n")
    for punto in puntos_agenda:
        print(f"Punto de agenda: {punto}")
        total_palabras = defaultdict(int)
        total_participaciones = defaultdict(int)
        for participante in participantes:
            participaciones = transcripciones.get((punto, participante), [])
            total_participaciones[participante] = len(participaciones)
            total_palabras[participante] = sum(len(participacion.split()) for participacion in participaciones)
            print(f"{participante}: {total_participaciones[participante]} participaciones, {total_palabras[participante]} palabras totales")
        print("\n")

# Registrar los puntos de la agenda y la lista de participantes
puntos_agenda = registrar_punto_agenda()
participantes = registrar_participantes()

# Transcribir las participaciones de los miembros
transcripciones = {}
for punto in puntos_agenda:
    for participante in participantes:
        participacion = transcribir_participacion(punto, participante)
        transcripciones[(punto, participante)] = transcripciones.get((punto, participante), []) + [participacion]

# Generar el informe de la sesión
generar_informe(participantes, puntos_agenda, transcripciones)