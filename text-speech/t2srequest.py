import speech_recognition as sr 
import webbrowser as wb 


def main():
    r1 = sr.Recognizer() #case youtube
    r2 = sr.Recognizer() #spring
    r3 = sr.Recognizer() # entrer caption

    with sr.Microphone() as source:
        print("Choix List-> [search google ; search youtube]")
        print("Speak now [first or second]...")
        audio = r3.listen(source)

    if 'first' in r2.recognize_google(audio):
        r2 = sr.Recognizer() #re-init 
        url_google =  'https://www.google.com/search?q='
        with sr.Microphone() as source:
            print('\n Search your query ')
            audio = r2.listen(source)

            try:
                get = r2.recognize_google(audio)
                print('\n '+get)
                wb.open_new(url_google+get) #open browser

            except sr.UnknownValueError as e:
                print('Error: '+str(e))
            except sr.RequestError as e: 
                print('failed: {}'.format(e))


    if 'second' in r1.recognize_google(audio):#case video
        r1 = sr.Recognizer() #re-init 
        url_ =  'https://www.youtube.com/results?search_query='
        with sr.Microphone() as source:
            print('\n Search your query ')
            audio = r1.listen(source)

            try:
                get = r1.recognize_google(audio)
                print('\n '+get)
                wb.open_new(url_+get) #open browser

            except sr.UnknownValueError as e:
                print('Error: '+str(e))
            except sr.RequestError as e: 
                print('failed: {}'.format(e))

if __name__ == "__main__":
    print('Dans ce program dire une expression qui contient First- > recheche google')
    print('et Second - > recheche you tube')
    main()
