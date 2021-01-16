
import sqlite3 

class Database(): 

    conn = None 

    def __init__(self, fileName = "data.db"):
        self.conn = sqlite3.connect(fileName)
        try: 
            self.initializeTables()
            print("DB Initialized")
        except sqlite3.OperationalError as e: 
            print(e)
            print("Loaded DB ")
        except Error as e: 
            print(e)
    
    def __del__(self):
        self.conn.close()

    def initializeTables(self):    
        self.conn.execute("""
            CREATE TABLE Task 
            (taskid INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL, 
            description TEXT NOT NULL);
        """)
        self.conn.execute("""
            CREATE TABLE SPRINT(
                sprintid INTEGER PRIMARY KEY AUTOINCREMENT,
                sprintname TEXT NOT NULL, 
                taskid, integer, 
                FOREIGN KEY(taskId) REFERENCES Task(taskid) ON DELETE CASCADE
            );
        """)

    def addTask(self, taskName, taskDescription): 
        self.conn.execute(
            f"""
            INSERT INTO Task(title,description) VALUES('{taskName}', '{taskDescription}');

            """
        )
        self.conn.commit()
        print("taskadded")

    def getTasks(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Task")

        data = cur.fetchall()
        for row in data: 
            print(row)

if __name__ == "__main__": 
    db = Database()
    db.addTask("Task3", "description for task3")
    db.addTask("Task2", "description for task2")
    db.addTask("Task4", "description for task4")
    db.getTasks()
