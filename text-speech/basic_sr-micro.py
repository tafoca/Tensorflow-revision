import speech_recognition as sr
# case source stream is my microphone
def main():
    # init regonizer of audio
    r = sr.Recognizer()

    #definite source of stream data income
    with sr.Microphone() as source: 
        #invitation message 
        print('Say anithing!')
        #get audio to source
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said : {}'.format(text))
        except:
            print('Sorry can not reconize audio ')
            
if __name__ = "__main__": 
    main()
    
