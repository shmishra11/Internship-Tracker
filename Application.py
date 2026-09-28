from datetime import datetime
class Application:
    def __init__(self, company, city, title, date, status):
        
        self.company = company
        self.city = city
        self.title = title
        self.date = Application.is_valid_date(date)
        self.status = Application.is_valid_status(status)

    def get_company(self):
        return self.company

    def set_company(self, value):
        self.company = value

    def get_city(self):
        return self.city

    def set_city(self, value):
        self.city = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def get_date(self):
        return self.date

    def set_date(self, value):
        self.date = Application.is_valid_date(value)

    def get_status(self):
        return self.status

    def set_status(self, value):
        self.status = Application.is_valid_status(value)

    def __str__(self):
        return (
            f"{self.company} | {self.city} | {self.title} | {self.date.strftime('%Y-%m-%d')} | {self.status}"
        )

    def is_valid_date(date):
        date_format = "%Y-%m-%d"
        while True:
            try:
                t = datetime.strptime(date, date_format)
                return t
            except ValueError:
                date = input("Invalid Date. Try Again. Format - (YYYY-MM-DD): ")

    def is_valid_status(status):
        possible = [
            "Saved", "Applied", "Under Consideration", "OA", "Interview", "Final Interview", "Offer", "Rejected", "Withdrawn"
            ]
        while status not in possible:
            status = input("Invalid Status, Please Try Again: ")

        return status
