import os
import time
import pyfiglet
def selector(option):
  while option != 0:
    if option == 1:
      addition()
    elif option == 2:
      subtraction()
    elif option == 3:
      multiplication()
    elif option == 4:
      division()
    elif option == 69:
      print('Nice...')
      time.sleep(1)
    elif option == 5:
      credits()
    elif option == 6:
      area_menu()
    else:
        print("Invalid option.")
        time.sleep(1)
    print()
    menu()
    option = int(input("Enter your option: "))
def banner(x):
  banner = banner = pyfiglet.figlet_format(x)
  print(banner)
def menu():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Calculator")
  print()
  print("[1] Addition                    [6] Area Finder")
  print("[2] Subtraction                 [7] ???")
  print("[3] Multiplication              [8] ???")
  print("[4] Division                    [9] ???")
  print("[5] Credits                     [10] ???")
  print()
def addition():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Addition")
  number1 = int(input("First number: "))
  print() 
  number2 = int(input("Second number: "))
  result = number1 + number2
  print(f"{number1} + {number2} = {result}")
  time.sleep(2)
def multiplication():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Multiplication")
  number1 = int(input("First number: "))
  print() 
  number2 = int(input("Second number: "))
  result = number1 * number2
  print(f"{number1} * {number2} = {result}")
  time.sleep(2)
def division():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Division")
  number1 = int(input("First number: "))
  print() 
  number2 = int(input("Second number: "))
  result = number1 / number2
  print(f"{number1} / {number2} = {result}")
  time.sleep(2)
def subtraction():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Subtraction")
  number1 = int(input("First number: "))
  print() 
  number2 = int(input("Second number: "))
  result = number1 - number2
  print(f"{number1} - {number2} = {result}")
  time.sleep(2)
def credits():
  os.system('cls' if os.name == 'nt' else 'clear')
  banner("Credits")
  print()
  print("Made by Peyoway as a first real python project. Nothing revolutionary.")
  print()
  input("Press enter to continue.")

#-- Area here --
def area_square():
  print("")
  z = int(input("Get one side length of the square: "))
  result = z * z
  print(f"The area of the square is {result}")
  time.sleep(1)
def area_rectangle():
  l = int(input("Enter the length of the rectangle. "))
  print()
  w = int(input("Enter the width of the rectangle."))
  result = l * w
  print()
  print(f"The area of the rectangle is {result}")
def area_triangle():
  b = int(input("Enter the base of the triangle."))
  h = int(input("Enter the height of the rectangle."))
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
    elif figure == 4:
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


