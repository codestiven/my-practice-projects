import pyautogui, webbrowser
from time import sleep
import random


# Abre WhatsApp Web con el número indicado
webbrowser.open('https://web.whatsapp.com/send?phone=' + "8292031165") 

sleep(10)  # Tiempo para cargar WhatsApp Web

# Lista de frases para enviar
frases = [
    "¡Buen chiste, amigo!",
    "Eso fue épico 😂",
    "Me hizo reír mucho 🤣",
    "Eres un genio del humor 🤩",
    "¡Qué buenísimo estuvo eso!",
    "No puedo parar de reír 😂😂",
    "Tienes un don para los chistes 😄",
    "¡Lo mejor que he escuchado hoy!",
    "Gracias por alegrarme el día 😊",
    "Sigue así, comediante en potencia 😎",
    "te esta gustando maamguebaso!",
    "XD",
    "ESTO SERA INFINITO!nO PUEDO PARAR DE RER "
]

# Bucle infinito para enviar mensajes
while True:
    frase_aleatoria = random.choice(frases)  # Selecciona una frase aleatoria
    pyautogui.typewrite(frase_aleatoria)
    pyautogui.press('enter')
    sleep(0.5)  # Espera 2 segundos entre mensajes