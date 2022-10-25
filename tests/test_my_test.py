# import pytest
# import requests
#
#
# def stest_ex10():
#     phrase = input("Set a phrase: ")
#     print(phrase)
#
#     assert len(phrase) <= 15, "Длина строки больше 15 символов"
#
#
# def stest_ex11():
#     responce = requests.get("https://playground.learnqa.ru/api/homework_cookie")
#     testValue = responce.cookies.get('HomeWork')
#     print(testValue)
#     expectedCookiesValue = 'hw_value'
#
#     assert testValue == expectedCookiesValue, f"Cookies values is not correct, {testValue} is actual value, " \
#                                               f"expected value is {expectedCookiesValue}"
#
#
# def stest_ex12():
#     responce = requests.get("https://playground.learnqa.ru/api/homework_header")
#     testValue = responce.headers.get('x-secret-homework-header')
#     print(testValue)
#     expectedHeadersValue = 'Some secret value'
#
#     assert testValue == expectedHeadersValue, f"Headers values is not correct, {testValue} is actual value, " \
#                                               f"expected value is {expectedHeadersValue}"
#
#
# userAgentList = {
#     "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) "
#     "Version/4.0 Mobile Safari/534.30",
#     "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 "
#     "Mobile/15E148 Safari/604.1",
#     "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 "
#     "Safari/537.36 Edg/91.0.100.0",
#     "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 "
#     "Mobile/15E148 Safari/604.1 "
# }
#
#
# @pytest.mark.parametrize("userAgent", userAgentList)
# def test_ex13(userAgent):
#     url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
#     responce = requests.get(url, headers={"User-Agent": userAgent})
#     actualPlatform = responce.json()["platform"]
#     actualBrowser = responce.json()["browser"]
#     actualDevice = responce.json()["device"]
#
#     if userAgent == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (" \
#                     "KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
#         expectedPlatform = 'Mobile'
#         expectedBrowser = 'No'
#         expectedDevice = 'Android'
#
#     elif userAgent == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) " \
#                       "CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
#         expectedPlatform = 'Mobile'
#         expectedBrowser = 'Chrome'
#         expectedDevice = 'iOS'
#
#     elif userAgent == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
#         expectedPlatform = 'Googlebot'
#         expectedBrowser = 'Unknown'
#         expectedDevice = 'Unknown'
#
#     elif userAgent == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
#                       "Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
#         expectedPlatform = 'Web'
#         expectedBrowser = 'Chrome'
#         expectedDevice = 'No'
#
#     else:
#         expectedPlatform = 'Mobile'
#         expectedBrowser = 'No'
#         expectedDevice = 'iPhone'
#
#     assert actualPlatform == expectedPlatform, f"Incorrect Platform Values, {actualPlatform} - is actual value, " \
#                                                f"expected value is - {expectedPlatform}"
#     assert actualBrowser == expectedBrowser, f"Incorrect Browser Values, {actualBrowser} - is actual value, " \
#                                              f"expected value is - {expectedBrowser}"
#     assert actualDevice == expectedDevice, f"Incorrect Device Values, {actualDevice} - is actual value, " \
#                                            f"expected value is - {expectedDevice}"
