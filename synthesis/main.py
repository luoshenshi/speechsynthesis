import subprocess

try:
    import pyaudio
    import speech_recognition as sr

    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Apologies, the audio wasn't clear enough.")
    except sr.RequestError as e:
        print("There was an issue retrieving results. Error: {0}".format(e))
except ImportError:
    subprocess.check_call(["python", "-m", "pip", "install", "pyaudio"])
    subprocess.check_call(["python", "-m", "pip", "install", "SpeechRecognition"])

    print("\n\nInstalled the required packages. Now, rerun the code. This will happen only if the requirements are not satisfied.")
