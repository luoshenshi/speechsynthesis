import sys
sys.stdout.reconfigure(encoding='utf-8')
import subprocess

try:
    import pyaudio
    import speech_recognition as sr

    def recognize_speech(language_code=None):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # r.pause_threshold = 1
            print("readyCode1", flush=True)
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            if language_code:
                print(r.recognize_google(audio, language=language_code))
            else:
                print(r.recognize_google(audio))
        except sr.UnknownValueError:
            print("UnknownValueError")
        except sr.RequestError as e:
            print("There was an issue retrieving results. Error: {0}".format(e))

    if len(sys.argv) > 1:
        language_code = sys.argv[1]
        recognize_speech(language_code)
    else:
        recognize_speech()
except ImportError:
    subprocess.check_call(["python", "-m", "pip", "install", "pyaudio"])
    subprocess.check_call(["python", "-m", "pip", "install", "SpeechRecognition"])
