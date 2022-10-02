import requests

responce = requests.get("https://playground.learnqa.ru/api/long_redirect")
first = responce.history[0]
second = responce.history[1]
third = responce
print(first.url)
print(second.url)
print(third.url)
