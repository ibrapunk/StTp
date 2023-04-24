import speech_recognition as sr
import json
import datetime
import tkinter as tk
#Agenda

agenda = {}  # Diccionario para almacenar los apartados y los puntos de la agenda
seguir_agregando = True

while seguir_agregando:
    # Solicitar el apartado
    apartado = input("Ingrese el apartado de la agenda ( o 'T' para terminar): ")
    
    if apartado == 'T':
        seguir_agregando = False
    else:
        # Solicitar uno o varios puntos dentro del apartado
        puntos = []
        seguir_agregando_puntos = True
        while seguir_agregando_puntos:
            punto = input(f"Ingrese un punto para el apartado '{apartado}' ( o 'T' para terminar): ")
            if punto == "T":
                seguir_agregando_puntos = False
            else:
                puntos.append(punto)
        
        # Agregar el apartado y sus puntos a la agenda
        agenda[apartado] = puntos

# Imprimir la agenda
print("Agenda:")
for apartado, puntos in agenda.items():
    print(f"\n{apartado.upper()}")
    for punto in puntos:
        print(f"- {punto}")

#Nombre de los participantes
nombre_participantes = []

while True:
    nombre = input("Ingrese el nombre completo del participante ( o 'fin' para terminar la lista): ")
    if nombre.lower() == 'fin':
        break
    else:
        nombre_participantes.append(nombre)
print("La lista de participantes es: ", nombre_participantes)

#Reconocimiento de voz
r = sr.Recognizer()
cont=0
l=[]
with sr.Microphone() as source:
    while cont<10:
        
#seleccion de la persona que va a hablar
        print(nombre_participantes)
    n=input("Cual participante va a hablar? ")
    for x in nombre_participantes:
            if n == x:
                print ("Intervención:\n")
                print("Di algo...")
                audio = r.listen(source)
                cont=cont+1
                try:
                    print("iniciando el reconocimiento...\n")
                    text = r.recognize_google(audio, language='es-ES')
                    print(x + " ha dicho: " + text)
                    l.append(text)
                    if text=="salir":
                        break
                except sr.UnknownValueError:
                    print("No se pudo reconocer el audio.")
                except sr.RequestError as e:
                    print("No se pudo obtener respuesta desde el servicio de Google Speech Recognition: {0}".format(e))

    print (l)




"""
# Se asume que la información de las grabaciones se encuentra en un archivo JSON llamado "grabaciones.json"
with open("grabaciones.source", "r") as f:
    grabaciones = source.load(f)

# Inicializamos los diccionarios que utilizaremos para generar los reportes
participaciones = {}
palabras_reconocidas = {}
participaciones_por_punto = {}

# Recorremos cada grabación para analizar las participaciones y palabras reconocidas
for grabacion in grabaciones:
    apartados = grabacion["agenda"]["apartados"]
    for apartado in apartados:
        punto = apartado["punto"]
        participantes = apartado["participantes"]
        for participante in participantes:
            nombre = participante["nombre"]
            tiempo_inicio = participante["tiempo_inicio"]
            transcripcion = participante["transcripcion"]
            # Agregamos la participación al diccionario de participaciones
            if nombre not in participaciones:
                participaciones[nombre] = []
            participaciones[nombre].append({"punto": punto, "tiempo_inicio": tiempo_inicio, "transcripcion": transcripcion})
            # Contabilizamos la cantidad de palabras reconocidas por cada participante
            palabras = len(transcripcion.split())
            if nombre not in palabras_reconocidas:
                palabras_reconocidas[nombre] = 0
            palabras_reconocidas[nombre] += palabras
            # Agregamos la participación al diccionario de participaciones por punto de la agenda
            if punto not in participaciones_por_punto:
                participaciones_por_punto[punto] = {}
            if nombre not in participaciones_por_punto[punto]:
                participaciones_por_punto[punto][nombre] = 0
            participaciones_por_punto[punto][nombre] += 1

# Reporte de participaciones por punto de la agenda
print("Reporte de participaciones por punto de la agenda")
for punto, participantes in participaciones_por_punto.items():
    print(f"Punto de agenda: {punto}")
    print("Participantes:")
    for participante, cantidad in participantes.items():
        print(f"- {participante}: {cantidad} veces")
    print()

# Reporte de participaciones completas
print("Reporte de participaciones completas")
for participante, participaciones in participaciones.items():
    print(f"Participante: {participante}")
    for participacion in participaciones:
        punto = participacion["punto"]
        tiempo_inicio = datetime.fromtimestamp(participacion["tiempo_inicio"]).strftime('%Y-%m-%d %H:%M:%S')
        transcripcion = participacion["transcripcion"]
        print(f"- Punto de agenda: {punto}")
        print(f"  Tiempo de inicio: {tiempo_inicio}")
        print(f"  Transcripción: {transcripcion}")
    print()

# Reporte de palabras reconocidas por participante
print("Reporte de palabras reconocidas por participante")
for participante, palabras in sorted(palabras_reconocidas.items(), key=lambda x: x[1], reverse=True):
    print(f"{participante}: {palabras} palabras")
                

    
 
"""