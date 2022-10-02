import time
import requests

responce1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(responce1.text)
josn = responce1.json()
checkResponceBeforeReady = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": josn["token"]})
print(checkResponceBeforeReady.text)
statusFirstCheck = checkResponceBeforeReady.json()
if statusFirstCheck["status"] == "Job is NOT ready":
    print("Status is correct")
else:
    print("Error")
time.sleep(josn["seconds"])
checkResponceAfterReady = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": josn["token"]})
print(checkResponceAfterReady.text)
statusSecondCheck = checkResponceAfterReady.json()
if statusSecondCheck["status"] == "Job is ready" and statusSecondCheck["result"] == "42":
    print("Status is correct and result is not null")
else:
    print("Error")
