import requests

responce = requests.get("https://playground.learnqa.ru/api/hello")
print(responce.text)


secondResponce = requests.get("https://playground.learnqa.ru/api/get_text")
print(secondResponce.text)