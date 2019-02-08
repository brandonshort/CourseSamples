#takes a topic from the user and goes to that wiki page
#goes to a random link from the page that is also a wiki article
#does this for x jumps the user requests

import urllib.request
import random

def wiki(url):
    url = url.split("\"")
    if len(url) > 1:
        return url[1]

start = input("What Wiki page would you like to start at?\n")
num = eval(input("How many jumps?"))

start = "https://en.wikipedia.org/wiki/" + start

def jumper(start):
    web_page = urllib.request.urlopen(start)

    lines = web_page.read().decode(errors="replace")
    web_page.close()

    lines = lines.replace(">", "<").split("<")

    links = []

    for item in lines:
        if "href" in item and "wiki" in item and ".org" not in item:
            if len(item):
                links.append(wiki(item))

    page_links = []
    for link in links:
        if str(link) != "None":
            page_links.append("http://en.wikipedia.org" + str(link))
            
    i = 0
    while i < num:
        print("Jumping from:", start)
        start = random.choice(page_links)
        print("To:", start)
        i +=1


jumper(start)
