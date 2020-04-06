from gtts import gTTS
import os
#[comment] : pip install ffmpeg-python
from pydub import AudioSegment
from pydub.playback import play

#case google api gtts google text to speech
file_handle = open("text.txt","r")
myText = file_handle.read().replace("\n", " ")
language = 'en'
def main(): 
    
    output = gTTS(text=myText,
                  lang=language,
                  slow=False,#speed of playing
                  )
    output.save("ouput.mp3")#save audio in this name
    
    
    #os.system("start ouput.mp3") #start audio by default program reading
    sound = AudioSegment.from_mp3('ouput.mp3')
    play(sound)
if __name__ == "__main__":
    main()