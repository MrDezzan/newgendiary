import speech_recognition as sr


def speech():
    mic=sr.Microphone()
    r=sr.Recognizer()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        return r.recognize_google(audio, language="ru-RU")