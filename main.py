from Application import Application
from Database import Database

database = Database()
database.createTable()

def printAllApplications(app):
    if len(app) == 0:
        print("No Applications Uploaded to Database.")
    else:  
        print(f"{'ID':^5}|{'Company':^20}|{'City':^15}|{'Title':^25}|{'Date':^15}|{'Status':^20}")
        print('-' * 103)
        for i in app:
            id, company, city, title, date, status = i
            print(f"{id:^5}|{company:^20}|{city:^15}|{title:^25}|{date:^15}|{status:^20}")


# --------------------------------------------------
# OUTPUT
# --------------------------------------------------
Database.printMenu()
userdemand = input("Enter a command: ")
possiblecommands = "123456"

while True:
    if userdemand not in possiblecommands or len(userdemand) != 1:
        userdemand = input("Unable to Understand Command. Please Try Again: ")
    else:
        if userdemand == "1":
            print("Enter Required Information.")
            database.createApplication()
        elif userdemand == "2":
            print(database.getApplication())
        elif userdemand == "3":
            printAllApplications(database.getApplications())
        elif userdemand == "4":
            database.updateApplication()
        elif userdemand == "5":
            database.deleteApplication()
        elif userdemand == "6":
            print("Thank you for using this program!")
            break

        Database.printMenu()
        userdemand = input("Enter a Command: ")