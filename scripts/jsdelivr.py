#!/usr/bin/python
import sys

filename = sys.argv
filename = filename[1]

cdn = "https://cdn.jsdelivr.net/gh/awesomebible/images" + "/" + filename

print(cdn)
