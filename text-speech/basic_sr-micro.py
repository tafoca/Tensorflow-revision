import speech_recognition as sr
# case source stream is my microphone
def main():
    # init regonizer of audio
    r = sr.Recognizer()

    #definite source of stream data income
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        #invitation message 
        print('Please Say anithing! ...')
        #get audio to source
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You have said : {}'.format(text))
            
       
        except Exception as e:
            print('Error : '+str(e))
            
            
        with open("recordaudio.wav","wb") as f:
            f.write(audio.get_wav_data())
            
if __name__ == "__main__":
    main()