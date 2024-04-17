import sqlite3


class Data_Manager():
    def __init__(self):
        self.data = []
        ###################################################
        # Create a database if one does not already exist #
        ###################################################
        self.remind_conn = sqlite3.connect('reminders.db')
        # Create a cursor instance
        self.rc = self.remind_conn.cursor()
        self.create_Database()


    def create_Database(self):
        # Create table
        self.rc.execute("CREATE TABLE if not exists Reminders (ID integer, Title text, Time integer, Priority interger, Description text)")

        # Commit changes
        self.remind_conn.commit()

        # Close our connections
        self.remind_conn.close()


    def update_reminder_database(self, entry_id, title, time, priority, desc):
        self.remind_conn = sqlite3.connect('reminders.db')
        self.rc = self.remind_conn.cursor()
        self.rc.execute("INSERT INTO Reminders VALUES (?,?,?,?,?)",(entry_id, title, time, priority, desc))
        self.row_id = self.rc.lastrowid
        # Commit changes
        self.remind_conn.commit()

        # Close our connections
        self.remind_conn.close()
        return self.row_id


    def get_reminder_data(self):
        self.data = []
        self.remind_conn = sqlite3.connect('reminders.db')
        # Create a cursor instance
        self.rc = self.remind_conn.cursor()
        for row in self.rc.execute('select * from Reminders'):
            # print(row)
            self.data.append(row)

        # Commit changes
        self.remind_conn.commit()

        # Close our connections
        self.remind_conn.close()
        # return entry_id, title, time, priority, desc
        return self.data


    def delete_reminder_data(self, index):
        self.remind_conn = sqlite3.connect('reminders.db')
        # Create a cursor instance
        self.rc = self.remind_conn.cursor()
        self.rc.execute("DELETE FROM Reminders WHERE ID = ?", (index,))
        # Commit changes
        self.remind_conn.commit()

        # Close our connections
        self.remind_conn.close()
