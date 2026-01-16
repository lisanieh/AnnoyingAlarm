import requests
import pyaudio
import wave
import base64
import json
import argparse

'''
API description:

1. Please set token and language first.
2. language can be set "華語"、"台語"、"華台雙語"、"客語"、"英語"、"印尼語"、"粵語".
3. Supports any audio file format, the default is wav (16k sample rate and mono format).
4. If you want to set the punctuation function, please set the 'segment' parameter to 'True'.
5. You can set the path of the audio file or record it directly.
'''
class STT:
    
    def __init__(self, token="", language="華語"):

        self.token = token
        self.language = language
        self.lang2service = {
            "華語": "A017",
            "台語": "A018",
            "華台雙語": "A019",
            "客語": "A020",
            "英語": "A021",
            "印尼語": "A022",
            "粵語": "A023"
        }

    def request(self, audio_path):
  
        with open(audio_path, 'rb') as file:
            raw_audio = file.read()
        audio_data = base64.b64encode(raw_audio)

        data = {
            "token": self.token,
            "audio_data": audio_data.decode(),
            "audio_format": audio_path.split(".")[-1],
            "service_id": self.lang2service[self.language],
            "information": "True",
            "mode": "General", # General, Streaming, Segmentation, Bilingual
            "correction": "False",
            "streaming_id": None
        }

        response = requests.post("http://140.116.245.149:2802/asr", json=data)

        if response.status_code == 200:
            # decode success
            sentence = json.loads(response.text)["words_list"][0].replace("<SPOKEN_NOISE>", "").replace(" ","")
            ## print(sentence)
            return sentence
        elif response.status_code == 400:
            # bad request
            print(response.text)
            return "Request failed!"
        elif response.status_code == 500:
            # server internal error
            print(response.text)
            return "Request failed!"

if __name__ == "__main__":
    #### Setting ####
    parser = argparse.ArgumentParser()
    parser.add_argument(
            "--num",
            type=str,
            default="0"
            )
    arg = parser.parse_args()
    token = "put your token here"
    language = "華語"
    stt = STT(token=token, language=language)
    #################

    # audio_path = stt.record()
    audio_path = "recording"+arg.num+".wav"
    sentence = stt.request(audio_path=audio_path)
    print(sentence)
