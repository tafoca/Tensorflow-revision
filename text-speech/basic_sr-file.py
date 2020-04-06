import speech_recognition as sr
# case source stream is my file of type audio


def main():
    sound = "test.wav"
    # init regonizer of audio
    r = sr.Recognizer()

    # definite source of filestream data income
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        # invitation message
        print('Converting audio file to text ...!')
        # get audio to source
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('Converted audio is  : \n{}'.format(text))
        except Exception as e:
            print('Sorry can not reconize audio '+e)



if __name__ == "__main__":
    main()