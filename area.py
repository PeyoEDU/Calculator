import os
import time
import pyfiglet
from actions import banner, selector, menu
def area_square():
  print("")
  z = int(input("Get one side length of the square: "))
  result = z * z
  print(f"The area of the square is {result}")
  time.sleep(1)
def area_rectangle():
  l = int(input("Enter the length of the rectangle. "))
def area_triangle():
  pass
def area_parallelogram():
  pass
def area_selector():
  #fix this up later`
  figure = int(input("Enter your option: "))
  while figure != 0:
    if figure == 1:
      area_square()
    elif figure == 2:
      area_rectangle()
    elif figure == 3:
      area_triangle()
    elif figure == 4:6
      area_parallelogram()
    elif figure == 5:
      menu()
      option = int(input("Enter your option: "))
      selector(option)
    else:
        print("Invalid option.")
        time.sleep(1)
    print()
    area_menu()
    
def area_menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Area Finder")
  print("[1] Square")
  print("[2] Rectangle")
  print("[3] Triangle")
  print("[4] Parallelogram")
  print("[5] Quit to Main Menu")
  print()
  area_selector()

