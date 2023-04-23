import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Di algo...")
    audio = r.listen(source)

try:
    texto = r.recognize_google(audio, language='es-ES')
    print("Lo que dijiste fue: " + texto)
except:
    print("Lo siento, no pude entenderte")


import speech_recognition as sr
import pyttsx3

# Crea un objeto para reconocer la voz
r = sr.Recognizer()

# Crea un objeto para sintetizar voz
engine = pyttsx3.init()

# Define los integrantes de la sesión y sus nombres
integrantes = {
    "Juan": "Juan",
    "María": "María",
    "Pedro": "Pedro"
}

# Define los apartados de la agenda y sus puntos
agenda = {
    "Presentación": ["Saludos", "Introducción de los integrantes"],
    "Discusión de temas": ["Tema 1", "Tema 2", "Tema 3"],
    "Conclusiones": ["Resumen de la sesión", "Asignación de tareas"]
}

# Función para convertir texto a voz
def decir(texto):
    engine.say(texto)
    engine.runAndWait()

# Función para identificar el integrante que habla
def identificar_integrante(audio):
    try:
        # Utiliza el reconocedor de voz para convertir audio a texto
        texto = r.recognize_google(audio, language='es-ES')
        
        # Busca en el texto los nombres de los integrantes
        for nombre in integrantes.values():
            if nombre in texto:
                # Si se encuentra el nombre de un integrante, devuelve su nombre
                return nombre
        
    except:
        pass
    
    # Si no se identifica a ningún integrante, devuelve None
    return None

# Función para identificar el apartado de la agenda
def identificar_apartado(audio):
    try:
        # Utiliza el reconocedor de voz para convertir audio a texto
        texto = r.recognize_google(audio, language='es-ES')
        
        # Busca en el texto los nombres de los apartados de la agenda
        for apartado in agenda.keys():
            if apartado in texto:
                # Si se encuentra el nombre de un apartado, devuelve su nombre
                return apartado
        
    except:
        pass
    
    # Si no se identifica ningún apartado, devuelve None
    return None

# Función para procesar la agenda
def procesar_agenda():
    while True:
        # Pide al usuario que identifique el integrante que habla
        decir("Por favor, identifícate")
        with sr.Microphone() as source:
            audio = r.listen(source)
        integrante = identificar_integrante(audio)
        if integrante:
            break

    while True:
        # Pide al usuario que identifique el apartado de la agenda
        decir(f"{integrante}, ¿De qué apartado deseas hablar?")
        with sr.Microphone() as source:
            audio = r.listen(source)
        apartado = identificar_apartado(audio)
        if apartado:
            break
    
    # Imprime los puntos del apartado seleccionado
    puntos = agenda[apartado]
    print(f"{integrante} habló del apartado '{apartado}' y mencionó los siguientes puntos: {puntos}")

# Ejecuta el programa
while True:
    procesar_agenda()
    respuesta = input("¿Deseas continuar? (s/n) ")
    if respuesta.lower() == "n":
        break


import speech_recognition as sr

def registrar_participantes():
    # Inicializa el reconocimiento de voz
    r = sr.Recognizer()

    # Crea una lista vacía para almacenar los nombres de los participantes
    participantes = []

    # Pide al usuario que registre a cada participante uno por uno
    while True:
        # Pide al usuario que diga el nombre completo del participante
        print("Por favor, di el nombre completo del participante.")
        with sr.Microphone() as source:
            audio = r.listen(source)

        # Convierte el audio a texto utilizando el reconocimiento de voz
        try:
            nombre = r.recognize_google(audio, language="es-ES")
            print(f"Has dicho: {nombre}")
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            continue

        # Agrega el nombre del participante a la lista de participantes
        participantes.append(nombre)

        # Pregunta si desea registrar a otro participante
        respuesta = input("¿Deseas registrar a otro participante? (s/n) ")
        if respuesta.lower() == "n":
            break

    # Imprime la lista completa de participantes
    print("Lista de participantes:")
    for participante in participantes:
        print(participante)


def seleccionar_punto(agenda):
    # Imprime los apartados y puntos de la agenda enumerados según el orden de inserción
    print("Seleccione un punto de la agenda:")
    for i, apartado in enumerate(agenda):
        print(f"{i + 1}. {apartado[0]}")
        for j, punto in enumerate(apartado[1]):
            print(f"   {i + 1}.{j + 1}. {punto}")

    # Pide al usuario que seleccione el punto de la agenda
    while True:
        try:
            seleccion = input("Selecciona un punto de la agenda: ")
            apartado_index, punto_index = [int(index) - 1 for index in seleccion.split(".")]
            punto = agenda[apartado_index][1][punto_index]
            print(f"Seleccionaste el punto {punto} del apartado {agenda[apartado_index][0]}")
            return punto, agenda[apartado_index][0]
        except (ValueError, IndexError):
            print("Por favor, selecciona un punto válido")


import speech_recognition as sr
import datetime

def participacion(punto, participantes):
    # Imprime la lista de participantes
    print("Selecciona un participante:")
    for i, participante in enumerate(participantes):
        print(f"{i + 1}. {participante}")

    # Pide al usuario que seleccione un participante
    while True:
        try:
            seleccion = int(input("Selecciona un participante: "))
            participante = participantes[seleccion - 1]
            break
        except (ValueError, IndexError):
            print("Por favor, selecciona un participante válido")

    # Usa la librería SpeechRecognition para registrar la participación del participante en texto
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{participante}, estás en turno para hablar. Empieza cuando estés listo.")
        audio = r.listen(source)

    try:
        # Utiliza Google Speech Recognition para convertir el audio en texto
        texto = r.recognize_google(audio, language="es-MX")
    except sr.UnknownValueError:
        texto = "No se pudo reconocer lo que se dijo"
    except sr.RequestError as e:
        texto = f"No se pudo realizar la solicitud a Google Speech Recognition: {e}"

    # Registra la hora de inicio y finalización de la participación
    hora_inicio = datetime.datetime.now()
    hora_fin = datetime.datetime.now()

    # Imprime la participación registrada
    print(f"\n{participante} habló sobre el punto {punto}:")
    print(f"\"{texto}\"")
    print(f"Hora de inicio: {hora_inicio}")
    print(f"Hora de finalización: {hora_fin}\n")


import speech_recognition as sr
import pyttsx3
import datetime

# Creamos un reconocedor de voz
r = sr.Recognizer()

# Creamos un sintetizador de voz
engine = pyttsx3.init()

# Definimos la lista de participantes de la sesión
participantes = ['Juan Perez', 'Maria Gomez', 'Pedro Rodriguez']

# Definimos la lista de puntos de la agenda
agenda = {'Punto 1': 'Presentación de la propuesta', 'Punto 2': 'Discusión y aprobación del presupuesto'}

# Definimos la función para asociar el reconocimiento de voz con un punto de la agenda y un participante
def reconocer_voz(punto, participante):
    # Comenzamos a escuchar el audio
    with sr.Microphone() as source:
        print('Habla, {}...'.format(participante))
        audio = r.listen(source)

    # Utilizamos el reconocimiento de voz
    try:
        # Convertimos el audio en texto
        texto = r.recognize_google(audio, language='es-ES')

        # Obtenemos la hora actual
        hora_actual = datetime.datetime.now().strftime('%H:%M:%S')

        # Imprimimos la información reconocida
        print('Punto: {}\nParticipante: {}\nHora de inicio: {}\nTexto reconocido: {}\n'.format(punto, participante, hora_actual, texto))

        # Sintetizamos la respuesta
        engine.say('Entendido, {}.'.format(participante))
        engine.runAndWait()

        # Devolvemos el texto reconocido
        return texto

    except sr.UnknownValueError:
        # Si no se pudo reconocer el audio, volvemos a intentar
        print('No se pudo reconocer el audio. Inténtalo de nuevo.\n')
        return reconocer_voz(punto, participante)

# Definimos la función principal del programa
def main():
    # Mostramos los puntos de la agenda disponibles
    print('Puntos de la agenda:')
    for i, punto in enumerate(agenda.values()):
        print('{}: {}'.format(i+1, punto))
    print()

    # Solicitamos el punto a tratar
    punto_index = int(input('Selecciona el punto de la agenda que se abordará: '))
    punto_seleccionado = list(agenda.keys())[punto_index-1]

    # Solicitamos la lista de participantes de la sesión
    print('Lista de participantes:')
    for participante in participantes:
        print('- {}'.format(participante))
    print()

    # Comenzamos la discusión del punto de la agenda seleccionado
    while True:
        # Solicitamos el participante que tomará la palabra
        participante_index = int(input('Selecciona el número del participante que hablará: '))
        participante_seleccionado = participantes[participante_index-1]

        # Realizamos el reconocimiento de voz y lo asociamos con el punto de la agenda y el participante seleccionados
        reconocimiento = reconocer_voz(punto_seleccionado, participante_seleccionado)

        # Si se reconoció un texto, lo mostramos y pasamos al siguiente participante
        if reconocimiento:
            print('El participante {} dijo: {}'.format(participante_seleccionado, reconocimiento))
            print()
        # Si no se reconoció un texto, volvemos a solicitarlo
        else:
            print('No se pudo reconocer el audio. Inténtalo de nuevo.\n')

        # Si se discutieron todos los puntos de la agenda, terminamos la sesión
        if all(punto_discutido for punto_discutido in agenda_discutidos.values()):
            print('Se discutieron todos los puntos de la agenda. Se termina la sesión.')
            break

        # Si se discutió el punto de la agenda actual, pasamos al siguiente punto
        if participantes_discutidos[participante_index-1] and participante_index == len(participantes):
            # Marcamos el punto de la agenda como discutido
            agenda_discutidos[punto_seleccionado] = True
            print('El punto {} fue discutido por todos los participantes.'.format(punto_seleccionado))
            print()
            # Pasamos al siguiente punto de la agenda
            if not all(punto_discutido for punto_discutido in agenda_discutidos.values()):
                punto_index += 1
                punto_seleccionado = list(agenda.keys())[punto_index-1]
                print('Se pasa al siguiente punto de la agenda: {}\n'.format(punto_seleccionado))
            # Si se discutieron todos los puntos, terminamos la sesión
            else:
                print('Se discutieron todos los puntos de la agenda. Se termina la sesión.')
                break

def generar_reporte_reconocimiento_voz(agendas, participantes, participaciones):
    # Imprimir listado de puntos de la agenda
    print('Listado de puntos de la agenda:')
    for i, agenda in enumerate(agendas):
        print('{}: {}'.format(i+1, agenda))
    print()

    # Imprimir participaciones en cada punto de la agenda
    for i, agenda in enumerate(agendas):
        print('Punto {}: {}'.format(i+1, agenda))
        for participante in participantes:
            participaciones_punto = [p for p in participaciones if p['punto'] == agenda and p['participante'] == participante]
            if participaciones_punto:
                print('  Participante {}:'.format(participante))
                for p in participaciones_punto:
                    print('    - Hora: {}, Texto: {}'.format(p['hora_inicio'], p['texto']))
        print()

def generar_reporte_palabras_reconocidas(participaciones):
    palabras_reconocidas = {}
    for participante, participaciones_participante in participaciones.items():
        palabras_reconocidas[participante] = sum([len(participacion['texto'].split()) for participacion in participaciones_participante])

    # Ordenamos los participantes por la cantidad de palabras reconocidas de mayor a menor
    participantes_ordenados = sorted(palabras_reconocidas.items(), key=lambda x: x[1], reverse=True)

    # Mostramos la lista de participantes y su cantidad de palabras reconocidas
    print('Palabras reconocidas por participante:')
    for participante, palabras in participantes_ordenados:
        print('- {}: {}'.format(participante, palabras))

participaciones = {}

for punto in agenda:
    participaciones[punto] = {}
    for participante in participantes:
        participaciones[punto][participante] = {'participaciones': 0, 'palabras': 0}

# Obtenemos la información del participante y el punto actual
participante_info = participaciones[punto_seleccionado][participante_seleccionado]

# Actualizamos la cantidad de participaciones y palabras reconocidas
participante_info['participaciones'] += 1
participante_info['palabras'] += len(reconocimiento.split())

# Mostramos la cantidad de participaciones por punto de la agenda
for punto, participantes_info in participaciones.items():
    print('Punto de la agenda: {}'.format(punto))
    for participante, info in participantes_info.items():
        if info['participaciones'] > 0:
            print('- {} participó {} veces y dijo {} palabras'.format(participante, info['participaciones'], info['palabras']))
    print()
    
# Mostramos la cantidad de palabras reconocidas por participante
print('Cantidad de palabras reconocidas por participante:')
for participante in participantes:
    palabras = sum(info['palabras'] for info in participaciones.values() if participante in info)
    print('- {}: {} palabras'.format(participante, palabras))

# Inicializar el diccionario de participaciones
participaciones = {}

# Iterar sobre cada punto de la agenda
for punto in agenda_discutidos:
    participaciones[punto] = {}
    
    # Iterar sobre cada participante
    for participante in participantes_discutidos:
        participaciones[punto][participante] = {'participaciones': 0, 'palabras': 0}

# Iterar sobre cada transcripción de la sesión
for transcripcion in transcripciones:
    for segmento in transcripcion['segmentos']:
        # Obtener el punto y el participante de la transcripción
        punto = segmento['punto_agenda']
        participante = segmento['participante']
        
        # Actualizar la cantidad de participaciones y palabras del participante en el punto
        participaciones[punto][participante]['participaciones'] += 1
        participaciones[punto][participante]['palabras'] += len(segmento['texto'].split())

# Mostrar los resultados
for punto in participaciones:
    print(f"Punto de la agenda: {punto}")
    for participante in participaciones[punto]:
        participacion = participaciones[punto][participante]['participaciones']
        palabras = participaciones[punto][participante]['palabras']
        print(f"{participante}: {participacion} participaciones, {palabras} palabras")
    print()
