from gtts import gTTS
import os
#case google api gtts google text to speech
myText = ""
language = 'en'
def main(): 
    
    output = gTTS(text=myText,
                  lang=language,
                  slow=False,#speed of playing
                  )
    output.save("ouput.mp3")#save audio in this name
    
    os.system("start ouput.mp3") #start audio by default program reading
    
if __name__ == "__main__":
    main()