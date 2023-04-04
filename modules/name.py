#priority:0
from Panoptes import *
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from termcolor import colored
from tqdm import tqdm
from bs4 import BeautifulSoup
import time

@modules.new("Find address by name")
def find_addres():
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
