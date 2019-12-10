#!/usr/bin/python3
# This is a template for Python scripts

import urllib
import urllib.request
import json
from html.parser import HTMLParser



mywebpage = urllib.request.urlopen("https://www.google.com/")
print("Result Code is: " + str(mywebpage.getcode()))

data = mywebpage.read()
#print(data)
myjsonfile = json.loads(data)