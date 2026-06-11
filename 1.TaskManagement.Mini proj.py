import sqlite3

con=sqlite3.connect("taskmngmt.db")
c=con.cursor()

c.execute("PRAGMA foreign_keys=ON")

# ---------------- User Table Creation ---------------- #
c.execute("""
          CREATE TABLE IF NOT EXISTS User(
          Username TEXT,
          UserType TEXT,
          ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          Password TEXT NOT NULL
          );
""")
# ---------------- Task Table Creation ---------------- #
c.execute("""
          CREATE TABLE IF NOT EXISTS Task(
          Task TEXT,
          TaskID INTEGER,
          TaskStatus TEXT DEFAULT 'Pending',
          StartDate TEXT,
          EndDate TEXT DEFAULT NULL,
          EID INTEGER NOT NULL,
          FOREIGN KEY(EID) REFERENCES User(ID) ON DELETE CASCADE
          );
""")

# ---------------- User Registration  ---------------- #

def regfn():
  try:
    u=input("Enter Username: ")
    p=input("Enter Password: ")
    ut=input("Enter UserType: ")
    c.execute("""INSERT INTO User(username,password,usertype) 
             VALUES (?,?,?) """,(u,p,ut))
    con.commit()

    print("User Registered Successfully")

  except sqlite3.IntegrityError:
    print("Username already exists")



# ---------------- MANAGER FUNCTIONS ---------------- #

def managerloginfn():

    u=input("Enter Username: ")
    p=input("Enter Password: ")
    c.execute("SELECT * FROM User WHERE Username = ? AND Password = ?",(u,p))
    x=c.fetchone()
    if x:
      print("Hi",x[0],"Login Successful")
      manager_menu()


    else:
      print("Invalid Credentials")


def assign_task():

    try:
        empid = int(input("Enter Employee ID: "))
        task = input("Enter Task Name: ")
        taskid= int(input("Enter Task ID: "))
        status = input("Enter Task Status: ")
        start = input("Enter Start Date (YYYY-MM-DD): ")
        end = None


        c.execute("""
                   INSERT INTO Task(Task,TaskId, TaskStatus, StartDate, EndDate, EID)
                    VALUES (?, ?, ?, ?,?,?)""", (task,taskid, status, start,end, empid)
                  )

        con.commit()

        print("Task Assigned Successfully")

    except Exception as e:
        print("Error:", e)


def view_tasks():

    c.execute("SELECT * FROM Task ")

    for i in c.fetchall():
        print(i)


def delete_task():
    taskid = int(input("Enter employee id : "))
    c.execute("""DELETE FROM Task WHERE tid = ?""", (taskid,))
    con.commit()

    print("Task Deleted")

def delete_user():
    empid = int(input("Enter employee id : "))
    c.execute("""DELETE FROM User WHERE id = ?""", (empid,))
    con.commit()

    print("User Deleted")

def manager_menu():

    while True:

        print("===== MANAGER MENU =====")
        print("1. Assign Task")
        print("2. View All Tasks")
        print("3. Delete Task")
        print("4.Delete User")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            assign_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            delete_user()

        elif choice == "5":
            break

        else:
            print("Invalid Choice")

def employeeloginfn():

    u = input("Enter Username: ")
    p = input("Enter Password: ")
    c.execute("SELECT * FROM User WHERE Username = ? AND Password = ?", (u, p))
    x = c.fetchone()
    if x:
        print("Hi", x[0], "Login Successful")
        empid=int(input("Enter Employee ID: "))
        employee_menu(empid)

    else:
     print("Invalid Credentials")
     return

def view_employee_tasks(empid):

    c.execute("SELECT * FROM Task WHERE Eid = ?", (empid,))

    for i in c.fetchall():
        print(i)

def update_task(empid):

    st = input("Enter task status: ")
    de = input("Enter task end date: ")
    tid = int(input("Enter Task ID: "))
    c.execute("UPDATE Task SET TaskStatus = ?, EndDate WHERE Eid = ? AND TaskId", (st, de, id,tid))
    con.commit()


def employee_menu(empid):

      while True:

            print("===== EMPLOYEE MENU =====")
            print("1. View My Tasks")
            print("2. Update Task")
            print("3. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                view_employee_tasks(empid)

            elif choice == "2":
                update_task(empid)

            elif choice == "3":
                break

            else:
                print("Invalid Choice")


# ---------------- MAIN MENU ---------------- #

while True:

    print("===== TASK MANAGEMENT SYSTEM =====")
    print("1. Register User")
    print("2. Manager Login")
    print("3. Employee Login")
    print("4. Exit")

    choice=int(input("Enter your choice: "))

    if choice==1:
        regfn()

    elif choice==2:
        managerloginfn()


    elif choice==3:
        employeeloginfn()


    elif choice==4:
      print("Thankyou")
      break

    else:
     print("Invalid Choice")

