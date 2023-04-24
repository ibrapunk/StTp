from typing import Dict, List
from speech_recognition import Microphone, Recognizer
import datetime
import collections

#A continuacion la siguiente funcion es la encargada de registrar los apartados y sus respectivos subtemas,

def registrar_agenda() -> Dict[str, Dict[str, str]]:
    salida: Dict[str, Dict[str, str]] = {}
    
    
    while True:
        nombre = input("Nombre del apartado ('fin' para salir)> ")

        if nombre.lower() == "fin":
            return salida 
        salida[nombre] = {}
        """
    La funcion input va permitirnos agregar nombre a los aparatados. La variable "nombre" va a ser igual a lo que respondamos como apartado(ese sera el nombre del apartado)
    o bien el usuario puede digitar "fin" para acabar si ya no quiere agregar mas apartados al diccionario.
         """

        while True:
            subtema = input("Nombre del subtema ('fin' para salir)> ")
            if subtema.lower() == "fin":
                break
            salida[nombre][subtema] = {}
"""
   La funcion input va permitirnos agregar nombre a los subtemas. Acá la variable "subtema" va a ser igual a lo que digitemops 
   subtema dentro del apartado. 
"""
#La siguiente funcion nos va a permitir agregar(registrar) a los participantes.
def registrar_participantes() -> List[str]:
    salida: List[str] = []
    while True:
        nombre = input("registro:Nombre del participante ('fin' para terminar)> ")
        if nombre.lower() == "fin":
            return salida
        salida.append(nombre)
        """
        Acá definimos registar_participantes con la notación SnakeCase y la convertimos ne una lista string.
        la funcion input le pregunta al usuario por su nombre o puede escribir "fin" para salir si asi lo desea.
        en la variable "nombre" utilizamos la funcio lower() para que el usuario pueda digitar "fin" tanto en minuscula como mayuscula
        """

            #acá definimos la variable crear_entrada para asi almacenar, acomodar el orden y luego impirimir lo que deseamos
def crear_entrada(apartado,subtema,participante,texto):
    entrada = {"apartado":apartado,
               "subtema":subtema,
               "participante":participante,
               "Hora":datetime.datetime.now(),
               "texto":texto,
               }
    return entrada
    """
    La funcion datatime me permite guardar con fecha y hora, la cual utilizo para cuando el reconocimiento de voz inicie
    este se obtenga fecha y hora del inicio de la grabacion.
    La principal funcion de esta deinicion es almacenar, acomodar el orden y luego impirimir lo que deseamos en una forma bonita visualmente.
    """

#La siguiente funcion nos mostrará la agenda con los apartados y subtemas anteriormente registrados.
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
    """
    La variable "Agenda" como diccionario tiene almacenados los apartados y subtemas. En este caso nos mostrara en pantalla
    los nombres de los apartados anteriormente registrados enumerados comenzando por el 1 y podremos seleccionar el apartado que queremos con solo colocoar el indice.
    """
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
    """
    Cuando hemos seleccionado el apartado, la terminal nos mostrará los subtemas que ese apartado tenia registrados y los enumerará
    iniciando por el 1, podremos seleccionar el numero del subtema para asi continuar.
    """

#la siguiente funcio tiene almacenado todo lo anteriormente registrado en la agenda que es tipo diccionario string
#los participantes están registrados mediante una lista string

if __name__ == "__main__":
    print("Registrando agenda")
    agenda: Dict[str, Dict[str, str]] = registrar_agenda()
    print("Agenda registrada",  "Registrando participantes")
    participantes: List[str] = registrar_participantes()
    print("Participantes registrados")

    #Aca comienza el reconocimiento de vos luego de seleccionar al participante que tomará la palabra
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
            """
            La funcion "Recognizer" es la encargada de reconocer lo que el usuario habla y lo convierte en texto.
            El metodo "adjust_for_ambient_noise" lo que hace es que al haber un silencio de 5 Segundos(Asi lo tenemos establecido pero puede cambiarse)
            el microfono se desactivará y pasará todo lo dicho a texto.
            Esto se guardará en el apartado y subtema selecciuonado y con el nombre del integrante seleccionado anteriormente
            """
            #Acá la siguiente funcion nos permite preguntar si queremos acabar la sesion o cambiar de apartado,subtema o integrante
            reconocimiento.append(crear_entrada(ap,sub_ap,participante,texto))
            var = input("Digite cualquier tecla para continuar con la sesion o 'Digite fin para salir' ")
            if var=="fin":
                break
            #Acá estariamos haciendo el reporte 1
def reporte1(lista):
    for x in lista:
        print("Apartado: ",x["apartado"])
        print("Sub Apartado: ",x["subtema"])
        print("Participante: ",x["participante"])
        print("Hora: ",x["Hora"])
        print("Texto: ",x["texto"])
        print("\n")
"""
Aca vamos a imprimir el apartado, sub apartado, participante, hora de inicio y lo que dijo en la sesion.
"""
# en el reporte 2 vamos a separar las palabras que dijo cada uno de los integrantes y ordenar de mayor a menor
def ordenar_miembros_por_palabras(miembros, palabras_por_miembro):
    return sorted(miembros, key=lambda miembro: palabras_por_miembro[miembro], reverse=True)
def reporte2(rec,part):
    # creamos una lista vacía para almacenar la cantidad de palabras por participante
    lista = []

    for participante in part:
        #esta funcion es la encargada de contar las palabras por cada miembro
        contador_de_palabras = 0

        for registro in rec:
            # esta funcion de encargade ver que el registro corresponde al participante actual, contar las palabras en el texto y agregarlas al contador
            if registro["participante"] == participante:
                palabras = registro["texto"].split()
                contador_de_palabras += len(palabras)

        # esta funcion agrega la cantidad total de palabras del participante a la lista
        lista.append({"participante": participante, "cantidad": contador_de_palabras})

    # La siguiente funcion ordena la lista de participantes según la cantidad total de palabras, de mayor a menor
    lista_ordenada = ordenar_miembros_por_palabras(part, {p["participante"]: p["cantidad"] for p in lista})

    for participante in lista_ordenada:
        for p in lista:
            if p["participante"] == participante:
                print("Participante:", p["participante"])
                print("Cantidad:", p["cantidad"])
        
"""
La funcion split() nos permite dividir el texto en palabras, acá la utilizamos para que cada texto que dice cada participante
se divida por cantidad de palabras
La función "ordenar_miembros_por_palabras " toma como parámetros la lista de miembros y la cantidad total de palabras reconocidas para cada participante.
La función devuelve la lista ordenada de mayor a menor según la cantidad total de palabras reconocidas.

"""
print(reconocimiento, "\n")

while True:
    print("Bienvenido al menú de selección de reporte")
    print("1. reporte 1")
    print("2. reporte 2")
    print("3. reporte 3")
    print("4. Salir")

    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print("Ha seleccionado la Opción 1",reporte1(reconocimiento))
    
    elif opcion == "2":
        print("Ha seleccionado la Opción 2", reporte2(reconocimiento,participantes))
    
    elif opcion == "3":
        print("Ha seleccionado la Opción 3")
        
    elif opcion == "4":
        print("Hasta pronto!")
        break
    else:
        print("Opción inválida, intente de nuevo")
    
