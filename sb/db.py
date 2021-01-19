
import sqlite3

class BoardDatabase(): 

    conn = None 

    def __init__(self, fileName = "data.db"):
        self.conn = sqlite3.connect(fileName)
        try: 
            self.initializeTables()
            print("DB Initialized")
        except sqlite3.OperationalError as e: 
            if 'already exists' in e.__str__():     
                print("Loaded DB ")
            else: 
                print(e)
        except Exception as e: 
            print(e)
    
    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def initializeTables(self):    
        self.conn.execute("""
            CREATE TABLE Task 
            (taskid INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT UNIQUE NOT NULL, 
            description TEXT NOT NULL);
        """)
        self.conn.execute("""
            CREATE TABLE Sprint(
                sprintid INTEGER PRIMARY KEY AUTOINCREMENT,
                sprintname TEXT NOT NULL, 
                taskid INTEGER,
                status TEXT DEFAULT 'To Do' CHECK(status = 'To Do' OR status = 'In Progress' OR status = 'Done' OR status = 'Testing'), 
                UNIQUE(sprintname, taskid),
                FOREIGN KEY(taskId) REFERENCES Task(taskid) ON DELETE CASCADE
                ); 
        """)

    def addTask(self, taskName, taskDescription): 
        try: 
            self.conn.execute(
                f"""
                INSERT INTO Task(title,description) VALUES('{taskName}', '{taskDescription}');
                """
            )
            self.conn.commit()
            print("taskadded")
        except sqlite3.IntegrityError as e: 
            print("Task already exists")

    def removeTask(self, taskname): 
        try: 
            self.conn.execute(f"""
                DELETE FROM Sprint 
                WHERE taskid = {self.getTaskId(taskname)}; 
            """)
            self.conn.execute(
                f"""
                DELETE FROM Task
                WHERE title = '{taskname}'; 
                """
            )
            self.conn.commit()
            print(taskname, 'deleted')

        except Exception as e:
            print(e)

    def getAllTasks(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Task;")

        data = cur.fetchall()
        return data

    def getTask(self, taskname):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM Task WHERE title = '{taskname}';")
        return cur.fetchall()

    def getStatus(self, taskname, sprintname="Sprint1"): 
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT status 
            FROM Sprint 
            WHERE sprintname = '{sprintname}' AND taskid = {self.getTaskId(taskname)};
        """)
        return cur.fetchone()[0]

    def getSprintTasks(self, sprintname): 
        cur = self.conn.cursor()
        cur.execute(f"""
            SELECT Sprint.sprintname, Task.title, Task.Description, Sprint.status
            FROM Sprint LEFT JOIN Task ON Sprint.taskid = Task.taskid
            WHERE Sprint.sprintname = '{sprintname}'; 
        """)

        return cur.fetchall()

    def getTaskId(self, taskname): 
        cur = self.conn.cursor()
        cur.execute(f"SELECT taskid FROM Task WHERE title = '{taskname}'")

        return cur.fetchone()[0]

    def addTaskToSprint(self, taskname, sprintname): 
        try: 
            self.conn.execute(
            f"""
                INSERT INTO Sprint(sprintname,taskid)
                VALUES ('{sprintname}', {self.getTaskId(taskname)}); 
            """)
            self.conn.commit()
        
        except Exception as e: 
            print(e) 

    def removeTaskFromSprint(self, taskname, sprintname): 
        taskid = self.getTaskId(taskname)
        self.conn.execute(
        f"""
            DELETE FROM Sprint
            WHERE taskid = {taskid} AND sprintname = '{sprintname}'; 
        """)
        self.conn.commit()

    def changeStatus(self, taskname, status):
        self.conn.execute(f"""
            UPDATE Sprint SET status='{status}'
            WHERE sprintname = 'Sprint1' AND taskid = {self.getTaskId(taskname)};
        """
        )
        self.conn.commit()

    def getTaskWithStatus(self, status):
        cur = self.conn.cursor()

        cur.execute(f"""
            SELECT Task.title, Task.description
            FROM Sprint LEFT JOIN Task on Sprint.taskid = Task.taskid
            WHERE status = '{status}';
        """)
        return cur.fetchall()
        
def main():
    db = BoardDatabase()
    db.addTask("task1", "description for task1" )
    db.addTask("Task2", "description2")
    db.addTask("task1", "trying to add another task1 should fail")
    db.addTask("task3", "description3") 

    for row in db.getAllTasks():
        print(row)
    print(db.getTaskId('task3'))
    db.addTaskToSprint('Task2', 'sprint1')
    print(db.getSprintTasks('sprint1'))
    db.removeTaskFromSprint('Task2','sprint1')
    print(db.getSprintTasks('sprint1'))


if __name__ == "__main__": 
    main()
