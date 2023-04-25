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

#Línea para categorizar manualmente las intervenciones
participations = ["participación 1 de persona 1 en punto de agenda 1", 
                  "participación 2 de persona 2 en punto de agenda 1", 
                  "participación 3 de persona 3 en punto de agenda 2",
                  "participación 4 de persona 3 en punto de agenda 3"]



participation_tokens = [word_tokenize(participation.lower()) for participation in participations]

participation_count = Counter([(tokens[2], tokens[5]) for tokens in participation_tokens])
person_count = Counter([tokens[2] for tokens in participation_tokens])
agenda_count = Counter([tokens[5] for tokens in participation_tokens])
transcription = "Aquí iría la transcripción completa de la sesión."
total_words = count_words(transcription)

print("Transcripción completa:")
print(transcription)
print()

print("Número total de palabras reconocidas por persona:")
for person, count in person_count.items():
    words = count_words(" ".join([participation for participation in participations if person in participation]))
    print(person, words)
print()

print("Cantidad total de participaciones por persona:")
for person, count in person_count.items():
    print(person, count)
print()

print("Cantidad total de participaciones por punto de agenda:")
for agenda, count in agenda_count.items():
    print(agenda, count)
print()

print("Cantidad total de palabras reconocidas por punto de agenda:")
for agenda, count in agenda_count.items():
    words = count_words(" ".join([participation for participation in participations if agenda in participation]))
    print(agenda, words)
print()

print("Cantidad total de palabras reconocidas por participante y por punto de agenda:")
