#priority:0
from Panoptes import *
import os
@modules.new("Account search by e-mail")
def holehe_search():
    email = input("\nenter an e-mail : ")
    os.system(f"holehe {email}")