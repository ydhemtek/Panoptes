#priority:0
from Panoptes import *
import os

@modules.new("Account search by e-mail")
def holehe_search():
    email = input("\nenter an e-mail : ")
    os.system(f"holehe {email}")

@modules.new("Extract information from instagram account")
def ig_uname():
    username = input(
        "\nenter a username : "
    )
    instagramsessionid = input(
        "\nenter a instagramsessionid : "
    )
    os.system(f"toutatis -u {username} -s {instagramsessionid}")

@modules.new("Find out if the number is used on different websites")
def search_from_no():
    num = input(
        "\n[example] : 33 123456789"
        "\nenter a number with his country code : "
    )
    os.system(f"ignorant {num}")
