#priority:0
from Panoptes import *
import requests
import threading
from termcolor import colored
from bs4 import BeautifulSoup
import re

sites = [
    {
        "name": "youtube",
        "url": "https://www.youtube.com/@{}",
        "cookies" : "CONSENT=YES+cb.20210418-17-p0.it+FX+917; ",
        "expect" : {
            "title": "(^\w* - |^)YouTube$"
        }
    }
]

def check(site, uname):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": site["cookies"] if site["cookies"] else ""
    }
    url = site["url"].format(uname)
    r = requests.get(url, headers=headers)
    if "title" in site["expect"] :
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string
        if re.search(site["expect"]["title"], title):
            print(colored(f"{uname} found on {site['name']} {url}", "green"))
        else:
            print(colored(f"{uname} Not found {site['name']}", "red"))
    if "status" in site["expect"] :
        if r.status_code == site["expect"]["status"]:
            print(colored(f"{uname} found on {site['name']} {url}", "green"))
        else:
            print(colored(f"{uname} not found on {site['name']}", "red"))
@modules.new("Find a username on different social media")
def username():
    uname = input("\nenter a username : ")
    for site in sites:
        try :
            threading.Thread(target=check, args=(site, uname)).start()
        except :
            pass

