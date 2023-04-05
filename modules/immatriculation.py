#priority:0
from Panoptes import *
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from stem.process import launch_tor_with_config
from termcolor import colored
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
import subprocess
import time

@modules.new("Find information about a vehicle using a license plate")
def from_license_plate():
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

    im = str(input("\nEnter a license plate : "))
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
