#asks user for a website
#scans website for all links
#prints all links in a copy paste friendly version
#prints total number of links

import urllib.request

#asks for url and attempts to fix if full link not provided
url = input("What website would you like links from?\n")
if "http://www." or "https://www." not in url:
    if "www." in url:
        url = "http://" + url
    else:
        url = "http://www." + url

#reads all data from page and places into a variable for use
webpage = urllib.request.urlopen(url)
contents = webpage.read().decode(errors = "replace")
webpage.close()

#splits all html tags into list items and filters those with links
contents = contents.replace(">", "<").split("<")
filtered_list = []
for item in contents:
    if "href=" in item:
        filtered_list.append(item)

#again splits list around any potential websites            
split_list = []
for item in filtered_list:
    new = item.split('"')
    split_list.append(new)

count = 0

#prints item if it starts with http making it a usable link
for lst in split_list:
    for item in lst:
        if "http" in item[:4]:
            count += 1
            print(item)
print("There are", count, "links.")

