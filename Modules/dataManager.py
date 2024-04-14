import numpy
import sqlite3


class Data_Manager():
    def __init__(self):
        # Do some database stuff
        # Create a database or connect to one that exists
        self.task_conn = sqlite3.connect('tasks.db')
        self.remind_conn = sqlite3.connect('reminders.db')
        # Create a cursor instance
        self.tc = self.task_conn.cursor()
        self.rc = self.remind_conn.cursor()
    def create_Databases(self):
        # Create table
        self.tc.execute("""CREATE TABLE if not exists tasks (
                ID integer,
                Title text,
                Date text,
                Time text)
                """)

        self.rc.execute("""CREATE TABLE if not exists reminders (
                ID integer,
                Title text,
                Date text,
                Time text)
                """)

        # Commit changes
        self.task_conn.commit()
        self.remind_conn.commit()

        # Close our connections
        self.task_conn.close()
        self.remind_conn.close()

        # Test Data
        # self.Test_Data = [[1, "Catch up on account", "12/21/23", "9:00 pm.",
        #                    "Make sure to close the account for November and update December"],
        #                   [2, "Ultra-scan appointment", "12/21/23", "9:00 pm.",
        #                    "Find out when your appointment is scheduled for."]]

    def update_task_database(self, entry_id, title, date, time, desc):
        self.tc.execute("INSERT INTO tasks VALUES (:ID, Title, Date, Time, Description",
                        {'id': entry_id,
                         'Title': title,
                         'Date': date,  
                         'Time': time,
                         'Description': desc
                         })

    def update_reminder_database(self, entry_id, title, date, time, desc):
        self.rc.execute("INSERT INTO reminders VALUES (:ID, Title, Date, Time, Description",
                        {'id': entry_id,
                         'Title': title,
                         'Date': date,
                         'Time': time,
                         'Description': desc
                         })
