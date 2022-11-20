#!/usr/bin/python3

import favicon
import urllib.request
import sys

url = sys.argv[1]
icons = favicon.get(url)
icon = icons[0]
print(icon.url)

urllib.request.urlretrieve(icon.url, "icon.png")
