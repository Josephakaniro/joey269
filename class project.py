import speech_recognition as sr

m = sr.Recognizer()

#file = sr.AudioFile('AUD-20220823-WA0041.wav')

mic = sr.Microphone()

print('Hello, are you there?\nspeak up my dear!')
try:
    with mic as source:
        m.adjust_for_ambient_noise(source)
        sound = m.listen(source)

    answer = m.recognize_google(sound, show_all=True)

    print(answer['alternative'][0]['transcript'])
except:
    print('speak up!!')
