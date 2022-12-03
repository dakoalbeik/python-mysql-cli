import mysql.connector
from printModule import *



db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySql.1234!",
  database="leasing"
)

cursor = db.cursor(buffered = True)



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

