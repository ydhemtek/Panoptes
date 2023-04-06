#priority:0
from Panoptes import *
from bs4 import BeautifulSoup
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from stem.process import launch_tor_with_config
from termcolor import colored
from selenium.common.exceptions import NoSuchElementException
from tqdm import tqdm
import subprocess
import time

@modules.new("Find information of a company")
def enterp():
    print(colored("\nOnly in France /!\ ", "red"))

    options = ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    print("""
    [1] name of a leader
    [2] name of a company
    [3] by SIREN      
            """)

    number = int(input("Choose a number : "))

    if (number == 1):
        name = str(input("Enter a name : "))
        with Chrome(options=options) as driver:
            driver.get(f"https://www.societe.com/cgi-bin/search?champs={name}")
            time.sleep(3)
            button = driver.find_element(By.XPATH, '//*[@id="didomi-popup"]/div/div/div/span')
            button.click()
            time.sleep(2)
            for i in tqdm(range(4), desc="data processing...", unit="s", unit_scale=True):
                time.sleep(1)
            number_of_leader = driver.find_element(By.ID, "recap_dir_nb_recap")
            print(f"number of leaders with this name : {number_of_leader.text}\n")
            time.sleep(3)
            button2 = driver.find_element(By.XPATH, '//*[@id="bloc_recap_dir"]')
            button2.click()
            time.sleep(3)
            button3 = driver.find_element(By.XPATH, '//*[@id="result_dir"]/p/a')
            button3.click()
            time.sleep(2)
            for i in tqdm(range(4), desc="data processing...", unit="s", unit_scale=True):
                time.sleep(1)
            element = driver.find_element(By.XPATH, '//*[@id="search_details"]')
            print(element.text)
    if (number == 2):
        print("available soon")
    if (number == 3):
        print("available soon")