# Internship Application Tracker
A command-line internship application tracker built with **Python, SQLite, SQL, and Object-Oriented Programming (OOP)**. The application stores internship applications in a persistent SQLite database and allows users to create, view, update, and delete application records.

## Features
* Add internship applications
* View individual applications
* View all applications in a formatted table
* Update application information
* Delete applications with confirmation
* Track application status
* Validate dates and statuses
* Persistent SQLite database storage
* Auto-generated application IDs
* Parameterized SQL queries

## Technologies
* Python
* SQLite
* SQL
* Object-Oriented Programming

## Application Statuses
* Saved
* Applied
* Under Consideration
* OA
* Interview
* Final Interview
* Offer
* Rejected
* Withdrawn

## Project Structure
```text
Internship-Application-Tracker/
├── Application.py
├── Database.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Overview
* **Application.py** — Application class and input validation
* **Database.py** — SQLite database setup and CRUD operations
* **main.py** — Command-line interface and program flow

## Database
Applications are stored locally using SQLite.

Each application contains:
| Field   | Description                |
| ------- | -------------------------- |
| ID      | Unique application ID      |
| Company | Company name               |
| City    | Internship location        |
| Title   | Internship position        |
| Date    | Date of application        |
| Status  | Current application status |

## Usage
Run the program with:
```bash
python main.py
```

The main menu provides the following options:
```text
1. Add Application
2. View Application
3. View All Applications
4. Update An Application
5. Delete An Application
6. Exit The Program
```

## CRUD Operations
This project demonstrates the four fundamental database operations:
* **Create** — `INSERT`
* **Read** — `SELECT`
* **Update** — `UPDATE`
* **Delete** — `DELETE`

Parameterized SQL queries are used to pass user input safely into database operations.

## Future Improvements
* Search and filter applications
* Sort applications by date or status
* Application statistics and metrics
* CSV export
* Automated testing
* Improved error handling
* Additional database functionality

## License
This project is licensed under the MIT License.
