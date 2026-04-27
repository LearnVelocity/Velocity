import random
import time
import sys
import os

def startup():
    input("Press ENTER to open the Sandbox... ")
    exec(open("sandbox.py").read())

class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'  # Resets color and style

modified = "n"
status = ":blank"


if modified == "y":
    if status == ":blank":
        v = "n"
    elif status == "GTTP":
        v = "y"
    elif status == "fw":
        v = "y"
    else:
        print(tcolors.FAIL)
        sys.exit("[/] YOU ARE RUNNING A MODIFIED VERSION OF THE SOFTWARE THAT HAS AN INVALID STATUS.\nPLEASE CONTACT THE MAKER OF THIS MODIFIED VERSION TO FIX THIS OR FIX IT YOURSELF BY SETTING STATUS TO ':blank'.")






dyk = ["Did you know there's a special version of Velocity that is optimized to run on Windows Command Prompt called Velocity for Windows?","Did you know there was a version of Velocity that came out 1 whole year before the actual thing called McCMD?","Did you know you can email notdabenjamin@gmail.com for help on anything about Velocity?", "Did you know Velocity was built using Pycharm and VS Code, but is still not reccommended to run on?","Did you know Velocity has 4 different names? Velocity, LearnVelocity, UseVelocity, and Velocity.py!"]


print(f"{tcolors.HEADER}__     __           __                      __    __               \n/  |   /  |         /  |                    /  |  /  |              \n$$ |   $$ | ______  $$ |  ______    _______ $$/  _$$ |_    __    __ \n$$ |   $$ |/      \\ $$ | /      \\  /       |/  |/ $$   |  /  |  /  |\n$$  \\ /$$//$$$$$$  |$$ |/$$$$$$  |/$$$$$$$/ $$ |$$$$$$/   $$ |  $$ |\n $$  /$$/ $$    $$ |$$ |$$ |  $$ |$$ |      $$ |  $$ | __ $$ |  $$ |\n  $$ $$/  $$$$$$$$/ $$ |$$ \\__$$ |$$ \\_____ $$ |  $$ |/  |$$ \\__$$ |\n   $$$/   $$       |$$ |$$    $$/ $$       |$$ |  $$  $$/ $$    $$ |\n    $/     $$$$$$$/ $$/  $$$$$$/   $$$$$$$/ $$/    $$$$/   $$$$$$$ |\n                                                          /  \\__$$ |\n                                                          $$    $$/ \n                                                           $$$$$$/")
print(random.choice(dyk))
print(f"{tcolors.OKGREEN}[-] LOADING...")
time.sleep(2)
if modified == "y":
    print(f"{tcolors.WARNING}[-] YOU ARE RUNNING A MODIFIED VERSION OF THE SOFTWARE\n\nVerified = {v}\nIf verified = n, you are running a version of the software that is not verified by the owner of Velocity.\nIf verified = y, this version has been created and reviewed by the owner of Velocity.\nIt is highly recommended that you PROCEED WITH CAUTION if you are using an unverified version.\n")
    input(f"{tcolors.OKGREEN}[+] Press ENTER to continue...")
    startup()
else:
    startup()