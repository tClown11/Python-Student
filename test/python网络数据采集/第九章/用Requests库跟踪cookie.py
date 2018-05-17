# -*- coding: utf-8 -*-
import requests

params = {'user': 'ryan', 'password': 'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", data=params)
print("Cookie is set to:")
print("-----------")
print("Going to profile page...")
r = requests.get("http://pythonscraping.com/pages/cookies/profile.php", cookies=r.cookies)
print(r.text)