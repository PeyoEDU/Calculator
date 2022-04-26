#simply acts as a bootloader, find everything in actions.py
import time
from actions import *
menu()
option = int(input("Enter your option: "))
selector(option)
print("Thanks for using this program. Goodbye.")