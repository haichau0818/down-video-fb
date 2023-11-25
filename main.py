import re
import requests
import urllib.request

#Video link

link= input("Video Url: ")

# Real HTML Data
html= requests.get(link)

try:
    url=re.search('hd_src:"(.+?)"',html.text)[1]
    print("HD Video")
except:
    url=re.search('sd_src:"(.+?)"',html.text)[1]
    print("SD Video")

print("dowloading...")
urllib.request.urlretrieve(url,"FaceBook Video.mp4")
print("Dowload SuccessFull!")
