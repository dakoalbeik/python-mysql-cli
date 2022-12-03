import mysql.connector
import time
from printModule import *



db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySql.1234!",
  database="leasing"
)

cursor = db.cursor(buffered = True)

def readTable(db, cursor, index):
  tableName = MAIN_MENU_ITEMS[index]["tableName"]
  sql = f"SELECT * from {tableName}"
  try:
    cursor.execute(sql)
    db.commit()
    printSuccess("Success")
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

def main():
  isReading = isUserReading()
  printTitle("Main Page")
  printMainMenu()
  # get the index corrosponding to table name
  actionIndex = getUserAction()

  if isReading:
    readTable(db, cursor, actionIndex)
  else:
    writeTable(db, cursor, actionIndex)
  main()

# application entry point
main();

