import requests

responce = requests.get("https://playground.learnqa.ru/api/check_type")
print(responce.text)