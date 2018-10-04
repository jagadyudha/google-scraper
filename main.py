#!/usr/bin/python
#coded by jagad
#sorry my code is bad :(
#SARANGHAEYOOO~

from bs4 import BeautifulSoup
import urllib2
import requests

print ("   _                       _                 _ ")
print ("  (_) __ _  __ _  __ _  __| | __ _  __ _  __| |")
print ("  | |/ _` |/ _` |/ _` |/ _` |/ _` |/ _` |/ _` |")
print ("  | | (_| | (_| | (_| | (_| | (_| | (_| | (_| |")
print (" _/ |\__,_|\__, |\__,_|\__,_|\__, |\__,_|\__,_|")
print ("|__/       |___/             |___/             ")
print ("")

dork = raw_input("Masukan Dork! : ")
print ("")
url_1 = "https://www.google.com/search?q=" +dork
url_2 = requests.get(url_1)
lol = BeautifulSoup(url_2.text, "html.parser")

for i in lol.findAll('cite'):
    print "-> ", i.text
print ("")