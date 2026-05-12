from game import ejecutar_juego
from palabras import obtener_palabra


# EJERCICIO 1
def generar_pista(palabra):
    """
    Dada una palabra, devolver un string con letras y guiones.
    Ejemplo:
    "python" -> "p _ t _ o _"
    """
    """
    #Declara el inicio de la pista
    if len(palabra) % 2 == 0:
        pista = palabra[0] + "_"
    else:
        pista = palabra[0]
        
    #Genera las incognitas
    for letra in range(2, len(palabra), 2):
        if len(palabra) % 2 == 0:
            pista = pista + palabra[letra] + "_"
        else:
            pista = pista + "_" + palabra[letra]
    """
    pista = ""
    #Genera las incognitas para cada otra letra
    for letra in range(1, len(palabra), 2):
        pista = pista + "_" + palabra[letra]

    if len(palabra) > len(pista): #Genera la ultima incognita si la cantidad de digitos de palabra es impar (o mayor que pista)
        pista += "_"
        
    return pista

# EJERCICIO 2
def verificar_palabra(palabra, intento):
    """
    Debe devolver True si el intento es correcto, False si no.
    """
    if palabra == intento:
        return True
    else:
        return False
    
    pass


def calcular_puntaje(tiempo_restante, intentos_restantes):
    puntaje = tiempo_restante * 10 + intentos_restantes * 20
    return round(puntaje)
    pass


# Ejercicio Adicional
def actualizar_pista(pista: str, palabra):
    # Si me queda una letra por adivinar, no hago nada y devuelvo la misma pista que tenía
    minIncognitas = 1
    for i in range(len(palabra)):
        if pista[i] == "_": #Si es una incognita
            if pista.count("_") > minIncognitas: #Si hay mas que 1 incognita
                pista = pista[:i] + palabra[i] + pista[i + 1 :] #Reemplaza una incognita con la letra real
            print(pista)
            break
    
    return pista
    

    pass


# ---------------- MAIN ----------------
palabra = obtener_palabra()

ejecutar_juego(
    palabra,
    generar_pista,
    verificar_palabra,
    actualizar_pista,
    calcular_puntaje,
)
