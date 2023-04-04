import os
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from stem.process import launch_tor_with_config
from termcolor import colored
import requests
from geopy import distance
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
import os
import subprocess
from bs4 import BeautifulSoup
import time

print("\033[34m" + r"""
                                   __                 
___________    ____   ____ _______/  |_  ____   ______
\____ \__  \  /    \ /  _ \\____ \   __\/ __ \ /  ___/
|  |_> > __ \|   |  (  <_> )  |_> >  | \  ___/ \___ \ 
|   __(____  /___|  /\____/|   __/|__|  \___  >____  >
|__|       \/     \/       |__|             \/     \/ 
""" + "\033[0m")

menu = []

class option :
    def __init__(self,no,desc,f) :
        self.no = no
        self.desc = desc
        self.f = f

    def new(*args, **kwargs) :
        def inner(f) :
            r = option(args[0],args[1],f)
            menu.append(r)
        return inner

@option.new(1,"Account search by e-mail")
def option_1():
    email = input("\nenter an e-mail : ")
    os.system(f"holehe {email}")

@option.new(2,"Extract information from instagram account")
def option_2():
    username = input(
        "\nenter a username : "
    )
    instagramsessionid = input(
        "\nenter a instagramsessionid : "
    )
    os.system(f"toutatis -u {username} -s {instagramsessionid}")

@option.new(3,"Find out if the number is used on different websites")
def option_3():
    num = input(
        "\n[example] : 33 123456789"
        "\nenter a number with his country code : "
    )
    os.system(f"ignorant {num}")

@option.new(4,"Find address by name")
def option_4():
    print(colored("\nOnly in France /!\ ", "red"))
    prenom = str(input("\nEnter a first name: "))
    nom = str(input("\nEnter a name: "))
    address = str(input("\nEnter a zip code: "))

    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    with Chrome(options=options) as driver:
        driver.get(f"https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui={prenom}+{nom}&ou={address}&univers=pagesblanches&idOu=")
        for i in tqdm(range(3), desc="", unit="s", unit_scale=True):
            time.sleep(1)
        button = driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]')
        button.click()
        for i in tqdm(range(4), desc="Data processing...", unit="s", unit_scale=True):
            time.sleep(1)
        html = driver.execute_script("return document.documentElement.outerHTML;")
        soup = BeautifulSoup(html, "html.parser")
        count = 0
        total_count = len(soup.find_all("a"))
        for a in soup.find_all("a"):
            count += 1
            if count > 12 and count <= total_count - 4:
                print(a.text)

@option.new(5,"Find information about a vehicle using a license plate")
def option_5():
    print(colored("\nOnly in France /!\ \n", "red"))
    port = 9150
    try:
        output = subprocess.check_output(['lsof', '-i', f'TCP:{port}'])
        pid = int(output.split()[10])
        os.kill(pid, 9)
        print(f"Process listening on port {port} has been terminated.")
    except subprocess.CalledProcessError:
        print(f"No process listening on port {port} was found.") 
    except ProcessLookupError:
        print(f"Failed to terminate process listening on port {port}. Permission denied.")

    im = str(input("\nEntrer a license plate : "))
    tor_config = {
        'SocksPort': str(9150),
        'ControlPort': str(9151),
        'DataDirectory': './data',
        'Log': [
            'NOTICE stdout',
            'ERR stderr'
        ]
    }
    tor_process = launch_tor_with_config(config=tor_config)

    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    options.add_argument('--proxy-server=socks5://127.0.0.1:9150')
    with Chrome(options=options) as driver:
        driver.get("https://www.largus.fr/vendre-voiture/ma-voiture/immatriculation/")
        for i in tqdm(range(3), desc="", unit="s", unit_scale=True):
            time.sleep(1)
        text_area = driver.find_element(By.ID,"immatriculation")
        text_area.send_keys(f"{im}")
        text_area.send_keys(Keys.RETURN)
        time.sleep(3)
        for i in tqdm(range(4), desc="data processing...", unit="s", unit_scale=True):
            time.sleep(1)
        try : 
            marque = driver.find_element(By.CLASS_NAME, "voiture-marque-lib")
            modele = driver.find_element(By.CLASS_NAME, "voiture-modele-lib")
            date = driver.find_element(By.CLASS_NAME, "voiture-mec")
            print(f"\nCar brand : {marque.text}\n")
            print(f"Car model : {modele.text}\n")
            print(f"Date of circulation : {date.text}")
        except NoSuchElementException:
            print("\nNo information found.")
        time.sleep(3)
        tor_process.kill()


def find_nearest_place2(place1_coords, country_code, place2_params, place2_endpoint):
    place2_params["countrycodes"] = country_code
    response = requests.get(place2_endpoint, params=place2_params).json()

    nearest_place2 = None
    nearest_distance = None
    for location in response:
        coords = (float(location['lat']), float(location['lon']))
        distance_to_location = distance.distance(place1_coords, coords).km
        if not nearest_place2 or distance_to_location < nearest_distance:
            nearest_place2 = location['display_name']
            nearest_distance = distance_to_location
    return nearest_place2, nearest_distance

@option.new(6,"find a place closest to another place")
def option_6() :
    place1 = str(input("\nplace 1 : "))
    place2 = str(input("\nplace 2 : "))
    country_code = str(input("\n(exemple : FR) enter a country : "))
    km = int(input("\nenter a minimum km : "))
    limit1 = int(input(f"\nlimited number of {place1} : "))
    limit2 = int(input(f"\nlimited number of {place2} : "))

    place1_endpoint = "https://nominatim.openstreetmap.org/search"
    place1_params = {
        "q": f"{place1}",
        "format": "json",
        f"limit": {limit1},
        "addressdetails": 1
    }

    place2_endpoint = "https://nominatim.openstreetmap.org/search"
    place2_params = {
        "q": f"{place2}",
        "format": "json",
        f"limit": {limit2},
        "addressdetails": 1
    }
    for place1_location in requests.get(place1_endpoint, params=place1_params).json():
        place1_coords = (float(place1_location['lat']), float(place1_location['lon']))
        nearest_place2, nearest_distance = find_nearest_place2(place1_coords, country_code, place2_params, place2_endpoint)
        if nearest_distance <= km:
            print(f"\nThe nearest {place2} to {place1_location['display_name']} is {nearest_place2} ({nearest_distance:.2f} km away)")
            print(f"Full address: {nearest_place2}")
    if not nearest_place2:
        print("No information found.")
    find_nearest_place2(place1_coords, country_code, place2_params, place2_endpoint)

get_option = lambda no : [x for x in menu if x.no == no][0]

def main():
    while True:
        for i in menu :
            print(f"[{i.no}] {i.desc}")
        number = str(input("\nChoose a number : "))
        if str(number) not in [str(x.no) for x in menu] :
            print(f"\nCan't find tool {number}\n")
            exit()
        else:
            number = int(number)
            get_option(number).f()
            break

if __name__ == "__main__" :
    main()