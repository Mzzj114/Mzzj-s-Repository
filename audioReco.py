import json, requests
import speech_recognition as sr

api_key = "RCNWhG57kGkADEAgtuUrm9tG"
secret_key = "eX3X773quq30kN02TcwUf4nKtSsOcGRT"
sReco = sr.Recognizer()
usingLangu = "zh-CN"


def getAccToken():
    url = ("https://aip.baidubce.com/oauth/2.0/token?client_id=" + api_key + "&client_secret=" + secret_key +
           "&grant_type=client_credentials")

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get("access_token")


def audioTran(audio_file, acc_token):  # if I want api
    pass


def audioTran(audio_file):  # using sphinx
    test = sr.AudioFile(audio_file)
    with test as testt:
        audio = sReco.record(testt)
    res = sReco.recognize_sphinx(audio, language=usingLangu)  # translate locally


if __name__ == "__main__":
    test = sr.AudioFile("D:\\User\\download\\audio.wav")
    with test as testt:
        audio = sReco.record(testt)
    # res = sReco.recognize_google(audio, language="zh-CN")  #this only available when google is available
    # res = sReco.recognize_sphinx(audio, language="en-US")  # translate locally
    res = sReco.recognize_vosk(audio)


    print(type(res))
    print(res)
