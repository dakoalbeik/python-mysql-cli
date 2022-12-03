import mysql.connector
import time
from printModule import *



db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySql.1234!",
  database="leasing"
)

cursor = db.cursor()

def main():
  printTitle("Main Page")
  printMainMenu()
  # get the index corrosponding to table name
  actionIndex = getUserAction()
  # get the user input based on the selected table name
  data = MAIN_MENU_ITEMS[actionIndex]["getData"]();
  try:
    insertIntoTable(cursor, actionIndex, data)
    print("Statement after insert")
    db.commit()
    printSuccess("Record inserted successfully!")
    time.sleep(2)
    main();
  except mysql.connector.Error as err:
    printError("Error occured while saving data! Please try again")
    printError(err)
    input("Press 'Enter' to continue...")
    main()

# application entry point
main();

