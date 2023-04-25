import nltk #Natural Language Toolkit, biblioteca
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize #Permite separar cada palabra en una sentencia y convertirla en token
from collections import Counter #Counter es una clase para contar elementos en una lista o una cadena de texto

import speech_recognition as sr


def reconocimiento_de_voz(punto_agenda, persona_hablando, idioma): #Función para poder escribir manualmente los parámetros lugar de la agenda, la persona que habla y el idioma utilizado 
    # Crear un objeto de reconocimiento de voz
    r = sr.Recognizer() #Instancia de objeto en la librería 'Speech Recognition' Reconocimiento de habla y conversión del audio a texto.
    # Configurar el idioma de reconocimiento
    with sr.Microphone() as source: #Activación de micrófono
        r.adjust_for_ambient_noise(source) #Ajuste de sonido ambiente
    
    # Escuchar la entrada de audio
    with sr.Microphone() as source:
        print(f"{persona_hablando} está hablando sobre el punto de la agenda '{punto_agenda}'. Habla ahora.")
        audio = r.listen(source)
    
    # Realizar el reconocimiento de voz
    try:
        texto = r.recognize_google(audio, language=idioma)
        print(f"{persona_hablando} dijo: {texto}")
        # Aquí se debe guardar el texto reconocido junto con el punto de agenda y la persona correspondiente
    except sr.UnknownValueError:
        print("No se pudo reconocer el discurso")
    except sr.RequestError as e:
        print(f"No se pudo realizar el reconocimiento de voz; {e}")


def registrar_agenda():
    agenda = []
    while True:
        apartado = input("Ingrese el nombre del apartado de la agenda (o escriba 'fin' para terminar): ")
        if apartado.lower() == "fin":
            break
        puntos = []
        while True:
            punto = input("Ingrese el nombre del punto de la agenda (o escriba 'fin' para terminar el apartado): ")
            if punto.lower() == "fin":
                break
            puntos.append(punto)
        agenda.append((apartado, puntos))
    return agenda


def registrar_participantes():
    participantes = []
    while True:
        participante = input("Ingrese el nombre completo del participante o 'fin' para finalizar: ")
        if participante.lower() == "fin":
            break
        participantes.append(participante)
    return participantes


def count_words(transcription):
    tokens = word_tokenize(transcription.lower())
    return len(tokens)


def mostrar_menu():
    print("Bienvenido al programa de gestión de reuniones!")
    print("1. Ver la lista de apartados de la agenda")
    print("2. Ver la lista de puntos de la agenda")
    print("3. Ver la lista de participantes")
    print("4. Modificar la lista de apartados de la agenda")
    print("5. Modificar la lista de puntos de la agenda")
    print("6. Modificar la lista de participantes")


def menu_principal(agenda, participantes):
    while True:
        print("== MENÚ PRINCIPAL ==")
        print("1. Ver agenda")
        print("2. Ver participantes")
        print("3. Modificar agenda")
        print("4. Modificar participantes")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            ver_agenda(agenda)
        elif opcion == "2":
            ver_participantes(participantes)
        elif opcion == "3":
            modificar_agenda(agenda)
        elif opcion == "4":
            modificar_participantes(participantes)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def ver_agenda(agenda):
    print("== AGENDA ==")
    for i, (apartado, puntos) in enumerate(agenda, start=1):
        print(f"{i}. {apartado}")
        for j, punto in enumerate(puntos, start=1):
            print(f"  {i}.{j} {punto}")
    print()


def ver_participantes(participantes):
    print("== PARTICIPANTES ==")
    for i, participante in enumerate(participantes, start=1):
        print(f"{i}. {participante}")
    print()


def modificar_agenda(agenda):
    while True:
        print("== MODIFICAR AGENDA ==")
        print("1. Agregar apartado")
        print("2. Agregar punto de agenda")
        print("3. Eliminar apartado")
        print("4. Eliminar punto de agenda")
        print("5. Regresar al menú principal")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            apartado = input("Ingrese el nombre del nuevo apartado: ")
            agenda.append((apartado, []))
        elif opcion == "2":
            apartado_index = int(input("Ingrese el número del apartado: "))
            punto = input("Ingrese el nombre del nuevo punto de agenda: ")
            agenda[apartado_index-1][1].append(punto)
        elif opcion == "3":
            apartado_index = int(input("Ingrese el número del apartado a eliminar: "))
            del agenda[apartado_index-1]
        elif opcion == "4":
            apartado_index = int(input("Ingrese el número del apartado: "))
            punto_index = int(input("Ingrese el número del punto de agenda a eliminar: "))
            del agenda[apartado_index-1][1][punto_index-1]
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intente de nuevo.")


def modificar_participantes(participantes):
    while True:
        print("== MODIFICAR PARTICIPANTES ==")
        print("1. Agregar participante")
        print("2. Eliminar participante")
        print("3. Regresar al menú principal")
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            participante = input("Ingrese el nombre completo del nuevo participante: ")
            participantes.append(participante)
            print(f"Se ha agregado a {participante} a la lista de participantes.")
        elif opcion == "2":
            print("Lista de participantes:")
            for i, participante in enumerate(participantes):
                print(f"{i+1}. {participante}")
            participante_index = int(input("Ingrese el número del participante a eliminar: "))
            if participante_index < 1 or participante_index > len(participantes):
                print("El número de participante ingresado no es válido.")
            else:
                participante_eliminado = participantes.pop(participante_index - 1)
                print(f"Se ha eliminado a {participante_eliminado} de la lista de participantes.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

