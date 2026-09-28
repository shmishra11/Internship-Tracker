from Application import Application
import sqlite3
class Database: 

    def __init__(self):
        self.connection = sqlite3.connect("applications.db")
        self.cursor = self.connection.cursor()

    def createTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY,
                company TEXT,
                city TEXT,
                title TEXT,
                date TEXT,
                status TEXT
            )
        """)
        self.connection.commit()

    def createApplication(self):
        company = input("Enter Company Name: ")
        city = input("Enter City Name: ")
        title = input("Enter Job Title: ")
        date = input("Enter Date of Application (YYYY-MM-DD): ")
        status = input("Enter Current Status of Application: ")
        app = Application(company, city, title, date, status)
    
        id = self.addApplication(app)
        print("The following application added to your database.\n")
        print(f"ID: {id}")
        print(app)

    def addApplication(self, app):
        self.cursor.execute(
            '''
            INSERT INTO APPLICATIONS
            (company, city, title, date, status)
            VALUES (?, ?, ?, ?, ?)
            ''',
            (
                app.get_company(), 
                app.get_city(), 
                app.get_title(), 
                app.get_date().strftime("%Y-%m-%d"),
                app.get_status()
            )
        )
        id = self.cursor.lastrowid
        self.connection.commit()
        return id

    def updateApplication(self):
        id = input("Enter Application ID: ")

        self.cursor.execute(
        '''
        SELECT * FROM applications WHERE id = ?
        ''',
        (id,)
        )

        result = self.cursor.fetchone()
        if result is None:
            raise Exception("Application not Found")
        
        print(result)
        print("Which Information Would you like Updated: ")
        print("1. Company")
        print("2. City")
        print("3. Title")
        print("4. Date")
        print("5. Status")
        print("6. Cancel")

        userdemand = input("Enter a Command: ")
        while userdemand not in "123456" or len(userdemand) != 1:
            print("Unable to understand command. Please type number only.")
            userdemand = input("Enter a Command: ")

        if userdemand == "1":
            val = input("Enter New Company Name: ")
            self.cursor.execute(
            '''
            UPDATE applications
            SET company = ?
            WHERE id = ? 
            ''',
            (val, id,)
            )
            self.connection.commit()

            self.cursor.execute(
            '''
            SELECT * FROM applications WHERE id = ?
            ''',
            (id,)
            )
            result = self.cursor.fetchone()

            print("Application Updated.")
            print(result)

        elif userdemand == "2":
            val = input("Enter New City Name: ")
            self.cursor.execute(
            '''
            UPDATE applications
            SET city = ?
            WHERE id = ? 
            ''',
            (val, id,)
            )
            self.connection.commit()

            self.cursor.execute(
            '''
            SELECT * FROM applications WHERE id = ?
            ''',
            (id,)
            )
            result = self.cursor.fetchone()

            print("Application Updated.")
            print(result)

        elif userdemand == "3":
            val = input("Enter New Internship Title: ")
            self.cursor.execute(
            '''
            UPDATE applications
            SET title = ?
            WHERE id = ? 
            ''',
            (val, id,)
            )
            self.connection.commit()

            self.cursor.execute(
            '''
            SELECT * FROM applications WHERE id = ?
            ''',
            (id,)
            )
            result = self.cursor.fetchone()

            print("Application Updated.")
            print(result)

        elif userdemand == "4":
            val = Application.is_valid_date(input("Enter New Date: "))
            self.cursor.execute(
            '''
            UPDATE applications
            SET date = ?
            WHERE id = ? 
            ''',
            (val.strftime("%Y-%m-%d"), id,)
            )
            self.connection.commit()

            self.cursor.execute(
            '''
            SELECT * FROM applications WHERE id = ?
            ''',
            (id,)
            )
            result = self.cursor.fetchone()

            print("Application Updated.")
            print(result)

        elif userdemand == "5":
            val = Application.is_valid_status(input("Enter New Status: "))
            self.cursor.execute(
            '''
            UPDATE applications
            SET status = ?
            WHERE id = ? 
            ''',
            (val, id,)
            )
            self.connection.commit()

            self.cursor.execute(
            '''
            SELECT * FROM applications WHERE id = ?
            ''',
            (id,)
            )
            result = self.cursor.fetchone()

            print("Application Updated.")
            print(result)
    
        elif userdemand == "6":
            print("Update Canceled.")

    def getApplication(self):
        id = input("Enter Application ID: ")

        self.cursor.execute(
        '''
        SELECT * FROM applications WHERE id = ?
        ''',
        (id,)
        )
        result = self.cursor.fetchone()

        if result is None:
            raise Exception("Application Not Found.")

        return result

    def getApplications(self):
        self.cursor.execute(
        '''
        SELECT * FROM applications
        ''',

        )
        results = self.cursor.fetchall()
        return results

    def deleteApplication(self):
        id = input("Enter Application ID: ")
        self.cursor.execute(
            '''
            SELECT * FROM applications where id = ?
            ''',
            (id,)
        )
        result = self.cursor.fetchone()
        if result is None:
            raise Exception("Application Not Found.")

        print(result)
        confirm = input("Are you sure you want to delete this application (y/n): ")

        while confirm != "y" and confirm != "n":
            confirm = input("Please indicate your response with y or n. Would you like to delete this application: ")

        if confirm == "n":
            print("Application was not deleted.")

        elif confirm == "y":
            self.cursor.execute(
            '''
            DELETE from applications
            where id = ?
            ''',
            (id,)
            )
            self.connection.commit()
            print("Application Deleted.")    

    @staticmethod
    def printMenu():
        print(f"\n\n---------- Internship Tracker ----------  \n")
        print("Please type the number of the respective function you want executed.\n")
        print("1. Add Application.")
        print("2. View Application.")
        print("3. View All Applications.")
        print("4. Update An Application.")
        print("5. Delete An Application.")
        print("6. Exit The Program.")
