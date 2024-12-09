from gtts import gTTS
from playsound3 import playsound

texto = "Hola, este es un texto de prueba."
tts = gTTS(text=texto, lang="es")

# Guarda el archivo temporalmente
filename = "temp_audio.mp3"
tts.save(filename)

# Reproduce el archivo
playsound(filename)
