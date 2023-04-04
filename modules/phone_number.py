#priority:0
from Panoptes import *
import os

@modules.new("Find out if the number is used on different websites")
def search_from_no():
    num = input(
        "\n[example] : 33 123456789"
        "\nenter a number with his country code : "
    )
    os.system(f"ignorant {num}")
