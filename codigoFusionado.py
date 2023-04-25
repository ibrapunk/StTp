import speech_recognition as sr

# Agenda
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

# Nombre de los participantes
nombre_participantes = []

while True:
    nombre = input("Ingrese el nombre completo del participante ( o 'fin' para terminar la lista): ")
    if nombre.lower() == 'fin':
        break
    else:
        nombre_participantes.append(nombre)

print("La lista de participantes es: ", nombre_participantes)

# Reconocimiento de voz
r = sr.Recognizer()
cont = 0
l = []

with sr.Microphone() as source:
    while cont < 10:
        print("\nIntervención:\n")
        print("Di algo...")
        audio = r.listen(source)
        cont = cont + 1
        try:
            print("Inicia el reconocimiento...\n")
            text = r.recognize_google(audio, language='es-ES')
            print("Has dicho: " + text)

            # Verificar si el nombre de la persona está en la lista de participantes
            if text.lower() in [nombre.lower() for nombre in nombre_participantes]:
                print(f"{text} presente.")

            l.append(text)
            if text == "salir":
                break
        except sr.UnknownValueError:
            print("No se pudo reconocer el audio.")
        except sr.RequestError as e:
            print("No se pudo obtener respuesta desde el servicio de Google Speech Recognition: {0}".format(e))

print(l)
