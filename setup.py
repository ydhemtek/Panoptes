import os
import venv
import sys

def install() :
    venv.create("venv", with_pip=True)

    if os.name == "nt":
        os.system("venv\\Scripts\\pip3 install -r requirements.txt")
    else:
        os.system("venv/bin/pip3 install -r requirements.txt")

    if os.name == "nt":
        with open("run.bat", "w") as f:
            f.write("venv\\Scripts\\python.exe Panoptes.py")
    else:
        with open("run.sh", "w") as f:
            f.write(f"#!/bin/bash\n{os.getcwd()}/venv/bin/python3 {os.getcwd()}/Panoptes.py")
        os.system("chmod +x run.sh")
        os.system("ln -s run.sh run")
        if os.path.exists("/usr/bin/panoptes"):
            os.system("sudo rm -f /usr/bin/panoptes")
        os.system("sudo ln -s run.sh panoptes")
        os.system(f"sudo ln -s {os.getcwd()}/run.sh /usr/bin/panoptes")
        os.system("sudo chmod +x /usr/bin/panoptes")

def uninstall() :
    if os.name == "nt":
        os.system("del venv")
        os.system("del run.bat")
    else:
        print("Uninstalling...")
        os.system("sudo rm -rf venv")
        os.system("sudo rm -f run.sh")
        os.system("sudo rm -f run")
        os.system("sudo rm -f panoptes")
        os.system("sudo rm /usr/bin/panoptes")
        print("Uninstalled successfully !")

if __name__ == "__main__" :
    if len(sys.argv) == 2 :
        if sys.argv[1] == "install" :
            install()
        elif sys.argv[1] == "uninstall" :
            uninstall()
    else :
        print("Usage : python setup.py install/uninstall")