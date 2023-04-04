#priority:0
from Panoptes import *
import os

@modules.new("Extract information from instagram account")
def ig_uname():
    username = input(
        "\nenter a username : "
    )
    instagramsessionid = input(
        "\nenter a instagramsessionid : "
    )
    os.system(f"toutatis -u {username} -s {instagramsessionid}")
