import yiyanAPI
import pygame
from audioReco import sReco
from audioReco import sr
from tts import say

def startConversa():
    pass

def sound(dir,volume=1.0):
    # this a func
    pygame.mixer.init()
    pygame.mixer.music.load(dir)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def formalResult(resu):
    return "{\n  \"text\" : \"" + resu + "\"\n}"

def informalResult(resu):
    if resu.count('"') < 4:
        return "Not enough quotes in the string"
    start = resu.index('"', resu.index('"', resu.index('"') + 1) + 1) + 1
    end = resu.index('"', start)
    return resu[start:end]

def listen_trans(recognizer_instance):
    print("start recognize")
    with sr.Microphone() as source:
        audioData = recognizer_instance.listen(source,10)
    result = informalResult( recognizer_instance.recognize_vosk(audioData) )
    print("I think you said: ", result)
    return result

if __name__ == '__main__':
    print("start working")

    said = listen_trans(sReco)
    if "你好" in said:
        print("嗯")
        sound("D:\\User\\download\\ding.wav")

        said = listen_trans(sReco)
        say( yiyanAPI.yiyanRequest("用70字以内回答：" + said) )


    #print (result)

