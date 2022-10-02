import requests

responce1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(responce1.text)
paramForResponce2 = {"method": "HEAD"}
responce2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=paramForResponce2)
print(responce2.text)
paramForResponce3 = {"method": "GET"}
responce3 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=paramForResponce3)
print(responce3.text)
print("    ")
elem = ["GET", "POST", "PUT", "DELETE", "HEAD"]
for i in elem:
        testresponce1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": i})
        testresponce2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        testresponce3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        testresponce4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        testresponce5 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": i})
        testresponce6 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
        testresponce7 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
        testresponce8 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
        testresponce9 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
        testresponce10 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
        print(i + " Method")
        print("GET - " + testresponce1.text)
        print("POST - " + testresponce2.text)
        print("PUT - " + testresponce3.text)
        print("DELETE - " + testresponce4.text)
        print("HEAD - " + testresponce5.text)
        print("GET without params- " + testresponce6.text)
        print("POST without data - " + testresponce7.text)
        print("PUT without data - " + testresponce8.text)
        print("DELETE without data - " + testresponce9.text)
        print("HEAD without data - " + testresponce10.text)
        print("   ")

