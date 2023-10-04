# 填充API Key与Secret Key
import requests
import json
import tts

api_key = "2bw5WQZPMs8DTWd4iy8zjWBM"
secret_key = "YgjyFutjgu1e13GI1K9op3E4gMLENGkY"
access_token = "24.f9c59e0d8b7e64bde3808918aab80544.2592000.1698879466.282335-38623422"  # 2023/10/2

def getAccToken():
    url = ("https://aip.baidubce.com/oauth/2.0/token?client_id="+ api_key+"&client_secret="+secret_key+
           "&grant_type=client_credentials")

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json().get("access_token")


def yiyanRequest(text, acc_token=access_token, detail=False):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + acc_token

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": text
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    responseText = requests.request("POST", url, headers=headers, data=payload).text

    print("yiyan get request:\n", responseText)
    resJ = json.loads(responseText)
    if detail:
        return resJ
    else:
        return resJ["result"]

if __name__ == '__main__':

    print(access_token)
    res = yiyanRequest("你好",access_token)
    print(res.text)
    resJ = json.loads(res.text)
    tts.say(resJ["result"])
