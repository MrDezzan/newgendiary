import speech_recognition as sr
from deep_translator import GoogleTranslator

def speechen():
    mic = sr.Microphone()
    r = sr.Recognizer()
    
    with mic as source:
        r.adjust_for_ambient_noise(source)  # Настройка на фоновый шум
        print("Говорите...")
        audio = r.listen(source)
        
    recognized_text = r.recognize_google(audio, language="ru-RU")
    
    translated_text = GoogleTranslator(source='auto', target='en').translate(recognized_text)


