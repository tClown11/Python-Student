# -*- coding: utf-8 -*-
import requests

params = {'firstname':'Ryan','lastname':'Mithcell'}
r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)