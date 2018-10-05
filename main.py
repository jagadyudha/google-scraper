#!/usr/bin/python
### coded by jagad ###

from bs4 import BeautifulSoup
import urllib
import requests

print("")
print("    ###c0ded by jagad###        $$\                                       ")
print("  ------------------------      $$ |                                      ")
print(" $$$$$$\   $$$$$$$\ $$$$$$\   $$$$$$\    $$$$$$\   $$$$$$\  $$$$$$\$$$$\  ")
print("$$  __$$\ $$  _____|\____$$\  \_$$  _|  $$  __$$\  \____$$\ $$  _$$  _$$\ ")
print("$$ /  $$ |$$ /      $$$$$$$ |   $$ |    $$$$$$$$ | $$$$$$$ |$$ / $$ / $$ |")
print("$$ |  $$ |$$ |     $$  __$$ |   $$ |$$\ $$   ____|$$  __$$ |$$ | $$ | $$ |")
print("\$$$$$$$ |\$$$$$$$\\$$$$$$$ |$$\\$$$$  |\$$$$$$$\ \$$$$$$$ |$$ | $$ | $$ |")
print(" \____$$ | \_______|\_______|\__|\____/  \_______| \_______|\__| \__| \__|")
print("$$\   $$ |                                                                ")
print("\$$$$$$  |                                                                ")
print(" \______/                                                                 ")
print("")

dork = raw_input("(Input Dork!) : ")
pages_number = []
pages_number.append(0)

for pgs in range(1, 1000):
	if pgs % 10 == 0:
		pages_number.append(pgs)

print ("")
encoded = urllib.quote(dork)

for p in pages_number:
	pages = str(p)
	url_1 = "https://www.google.com/search?q=" +encoded +"&start=" +pages
	url_2 = requests.get(url_1)
	wow = BeautifulSoup(url_2.text, "html.parser")
	for i in wow.findAll('cite'):
		print ("Link grabbed dude !!!")
		output = i.text
		myfile = open('output.txt', 'a')
		myfile.write(output + "\n")
