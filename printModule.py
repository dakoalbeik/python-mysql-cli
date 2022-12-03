from messages import *
import mysql.connector
import os
import time


def readTable(db, cursor, index):
  tableName = MAIN_MENU_ITEMS[index]["tableName"]
  sql = f"SELECT * from {tableName}"
  try:
    cursor.execute(sql)
    db.commit()
    printTable(cursor, cursor.fetchall())
  except mysql.connector.Error as err:
    printError("Error occured while reading data! Please try again")
    printError(err)
    
  input("Press 'Enter' to continue...")

def writeTable(db, cursor, index):
  # get the user input based on the selected table name
  data = MAIN_MENU_ITEMS[index]["getData"]()
  try:
    insertIntoTable(cursor, index, data)
    db.commit()
    printSuccess("Record inserted successfully!")
    time.sleep(2)
  except mysql.connector.Error as err:
    printError("Error occured while saving data! Please try again")
    printError(err)
    input("Press 'Enter' to continue...")


def isUserReading(error = ""):
  printTitle("Welcome to python/mysql cli :)")
  if error: printSuccess(error)
  response = input("Would you like to (r)ead, or (w)rite? ")
  if response == "r": return True
  elif response == "w": return False
  else:
    return isUserReading("Only (r), or (w) are accepted!")

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

def printTable(cursor, results):    

    # copied and modified from stackoverflow.com
    # https://stackoverflow.com/questions/10865483/print-results-in-mysql-format-with-python
    
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 
    
    maxValues = [0] * len(results[0])
    for row in results:
        for j, column in enumerate(row):
            maxValues[j] = max(maxValues[j], len(str(column)))

    for i, cd in enumerate(cursor.description):
        widths.append(max(maxValues[i], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += ' %-'+'%ss |' % (w,)
        separator += '-'*w + '--+'

    print(f'\n{separator}')
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)