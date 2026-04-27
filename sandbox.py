import random
import time

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

dyk = ["Did you know there's a special version of Velocity that is optimized to run on Windows Command Prompt called Velocity for Windows?","Did you know there was a version of Velocity that came out 1 whole year before the actual thing called McCMD?","Did you know you can email notdabenjamin@gmail.com for help on anything about Velocity?", "Did you know Velocity was built using Pycharm and VS Code, but is still not reccommended to run on?","Did you know Velocity has 4 different names? Velocity, LearnVelocity, UseVelocity, and Velocity.py!"]

print("\n" * 100)
print(f"{tcolors.HEADER}__     __           __                      __    __               \n/  |   /  |         /  |                    /  |  /  |              \n$$ |   $$ | ______  $$ |  ______    _______ $$/  _$$ |_    __    __ \n$$ |   $$ |/      \\ $$ | /      \\  /       |/  |/ $$   |  /  |  /  |\n$$  \\ /$$//$$$$$$  |$$ |/$$$$$$  |/$$$$$$$/ $$ |$$$$$$/   $$ |  $$ |\n $$  /$$/ $$    $$ |$$ |$$ |  $$ |$$ |      $$ |  $$ | __ $$ |  $$ |\n  $$ $$/  $$$$$$$$/ $$ |$$ \\__$$ |$$ \\_____ $$ |  $$ |/  |$$ \\__$$ |\n   $$$/   $$       |$$ |$$    $$/ $$       |$$ |  $$  $$/ $$    $$ |\n    $/     $$$$$$$/ $$/  $$$$$$/   $$$$$$$/ $$/    $$$$/   $$$$$$$ |\n                                                          /  \\__$$ |\n                                                          $$    $$/ \n                                                           $$$$$$/")
print(random.choice(dyk))
print(f"{tcolors.OKGREEN}[-] LOADING...")
time.sleep(2)
print(f"{tcolors.HEADER}WELCOME TO THE SANDBOX, User!")
print("Try !!Commands, or just straight in z")

