Task Management System:
Running the Application
Execute the Python file:
python task_management.py
The application will automatically create a SQLite database file named:
taskmngmt.db
if it does not already exist.
________________________________________
Main Menu
After starting the application, the following menu appears:
===== TASK MANAGEMENT SYSTEM =====

1. Register User
2. Manager Login
3. Employee Login
4. Exit
Register User
Create a new user by providing:
•	Username
•	Password
•	User Type
Example:
Enter Username: john
Enter Password: pass123
Enter UserType: Employee
________________________________________


Manager Operations
After successful login, managers can:
===== MANAGER MENU =====

1. Assign Task
2. View All Tasks
3. Delete Task
4. Delete User
5. Logout
Assign Task
Managers can assign tasks by entering:
•	Employee ID
•	Task Name
•	Task ID
•	Task Status
•	Start Date
Example:
Enter Employee ID: 1
Enter Task: Create Report
Enter Task ID: 101
Enter Task Status: Pending
Enter Start Date (YYYY-MM-DD): 2025-06-01
View All Tasks
View all tasks assigned to the employees.
Delete Task
Delete any particular task using task id.
Delete User
Delete any particular user using employee id.
________________________________________

Employee Operations
After successful login, employees can:
===== EMPLOYEE MENU =====

1. View My Tasks
2. Update Task
3. Logout
View My Tasks
Displays all tasks assigned to the logged-in employee.
Update Task
Allows employees to update:
•	Task Status
•	End Date
________________________________________
Database Schema
User Table
Column	Type
Username	TEXT
UserType	TEXT
ID	INTEGER PRIMARY KEY AUTOINCREMENT
Password	TEXT
Task Table
Column	Type
Task	TEXT
TaskID	INTEGER
TaskStatus	TEXT
StartDate	TEXT
EndDate	TEXT
EID	INTEGER
Foreign Key:
FOREIGN KEY(EID) REFERENCES User(ID) ON DELETE CASCADE

