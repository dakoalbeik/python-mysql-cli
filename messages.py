from enum import Enum
import datetime
import sql

class TYPE(Enum):
    INT = 1
    STRING = 2
    BOOL = 3

class COLOR:
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    BASE = "\033[0m"

def insertIntoTable(cursor, index, data):
    sql = MAIN_MENU_ITEMS[index]["sql"]
    cursor.execute(sql, data)

def getUserInput(msg, type = TYPE.STRING):
    message = msg;
    if(type == TYPE.BOOL):
        message += "\n1) Yes  2) No\n"
    response = input(f"{message} ")
    try:
        if not response.strip():
            raise ValueError();
        elif type == TYPE.INT:
            return int(response)
        elif type == TYPE.BOOL:
            num = int(response)
            if not num == 1 and not num == 2: raise ValueError()
            response = True if num == 1 else False
        return response;
    except ValueError:
        printError("Failed to parse user input!!")
        return getUserInput(msg, type)



def getApartmentInfo():
    return {
        "building_number" : getUserInput("Building number:", TYPE.INT),
        "apartment_number" : getUserInput("Apartment number:", TYPE.INT),
        "apartment_view" : getUserInput("Apartment view:"),
        "is_occupied" : getUserInput("Is it occupied:", TYPE.BOOL),
        "square_footage" : getUserInput("Square footage:", TYPE.INT),
        "room_count" : getUserInput("Rooms count (1 or 2):", TYPE.INT),
        "bathroom_count" : getUserInput("Bathrooms count (1 or 2):", TYPE.INT),
        "is_furnished" : getUserInput("Is it furnished:", TYPE.BOOL)
    }

def getApplicantInfo():
    return {
        "name" : getUserInput("Applicant name:"),
        "social_security" : getUserInput("Social security:"),
        "income" : getUserInput("Applicant income:", TYPE.INT),
        "email" : getUserInput("Applicant email:"),
        "phone_number" : getUserInput("Phone Number:"),
        "contact_date" : datetime.date.today(),
    }
    

def getApplicationInfo():
    return {
        "screening_result" : getUserInput("Screening result:"),
        "application_date" : datetime.date.today(),
        "applicant_id" : getUserInput("Applicant ID"),
    }

def getResidentInfo():
    return {
        "apartment_id" : getUserInput("Apartment ID:", TYPE.INT),
        "applicant_id" : getUserInput("Applicant ID:", TYPE.INT),
    }

def getMaintenenceOrdersInfo():
    return { 
        "details" : getUserInput("Provide a description:"),
        "order_status" : getUserInput("Status:"),
        "submission_date" : datetime.date.today(),
        "completion_date" : datetime.date.today() + datetime.timedelta(days=3),
        "resident_id" : getUserInput("Resident ID:", TYPE.INT),
    }

def getPetInfo():
    return {
        "name" : getUserInput("Pet name:"),
        "weight" : getUserInput("Pet weight (min 5 lb):", TYPE.INT),
        "pet_type" : getUserInput("Pet type:"),
        "color" : getUserInput("Pet color:"),
        "is_service_animal" : getUserInput("Is it a service animal:", TYPE.BOOL),
        "age" : getUserInput("Pet age:", TYPE.INT),
        "resident_id" : getUserInput("Resident ID:", TYPE.INT),
    }

def printError(error):
    print(f"{COLOR.RED}{error}{COLOR.BASE}")

MAIN_MENU_ITEMS = [
    {"name": "applicant", "getData": getApplicantInfo, "sql": sql.insertApplicant, "tableName": "applicants"},
    {"name": "resident", "getData": getResidentInfo, "sql": sql.insertResident, "tableName": "residents"},
    {"name": "apartment", "getData": getApartmentInfo, "sql": sql.insertApartment, "tableName": "apartments"},
    {"name": "maintenence order", "getData": getMaintenenceOrdersInfo, "sql": sql.insertMaintenenceOrder, "tableName": "maintenence_orders"},
    {"name": "pet", "getData": getPetInfo, "sql": sql.insertPet, "tableName": "pets"},
    {"name": "application", "getData": getApplicationInfo, "sql": sql.insertApplication, "tableName": "applications"}
]