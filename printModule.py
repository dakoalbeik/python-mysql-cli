from messages import *
import os

def getUserAction():
  response = input("")
  try:
    if not response.strip(): raise ValueError
    index = int(response[0]) - 1
    if(index >= 0 and index < len(MAIN_MENU_ITEMS)):
      name = MAIN_MENU_ITEMS[index]["name"].capitalize()
      printTitle(f"{name} Page")
      return index
    else: raise ValueError()
  except ValueError:
      printMainMenu("Error! Please enter a valid number!!")
      return getUserAction()

def printMainMenu(error = ""):
    if(error):
      printTitle("Main Page")
      printError(error)
    print("Enter a number to insert a corresponding entry:")
    for i, item in enumerate(MAIN_MENU_ITEMS):
      name = item["name"].capitalize()
      print(f"{i + 1}) {name}")
    

def printTitle(string):
  os.system('cls')
  LENGTH = 80
  string = f" {string} "
  OFFSET = (LENGTH - len(string)) // 2
  # 1-print ****
  text = ""
  for i in range(0, LENGTH):
    text += "*"
  print(text);
  # 2-print **<string>**
  text = ""
  for i in range(0, OFFSET):
    text += "*"
  text += COLOR.BLUE
  text += string;
  text += COLOR.BASE
  if len(string) % 2 != 0: 
    OFFSET += 1 
  for i in range(0, OFFSET):
    text += "*"
  print(text);
  # 3-print ****
  text = ""
  for i in range(0, LENGTH):
    text += "*"
  print(text);

def printSuccess(msg):
  print(f"{COLOR.YELLOW}{msg}{COLOR.BASE}")