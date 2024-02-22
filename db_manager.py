import sqlite3

class DataBaseManager:
    def __init__(self, database='carid.db'):
        self.connection = None
        self.database = database

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.database)
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def add(self, Username, carID):
        # Add a new user to the Users table
        conn = self.connect()
        cur = conn.cursor()
        # Assuming that the Users table has auto-increment ID, name and code columns
        cur.execute("INSERT INTO Users (Username, carID) VALUES (?, ?)", (Username, carID))
        conn.commit()

    def delete(self, carID):
        # Delete a user from the Users table by carID
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM Users WHERE carID = ?", (carID,))
        conn.commit()

    def delete_n(self, username):
        # Delete a user from the Users table by username
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM Users WHERE username = ?", (username))
        conn.commit()

    def modify(self, user_id, name, code):
        # Modify an existing user's name and code in the Users table by ID
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("UPDATE Users SET name = ?, code = ? WHERE id = ?", (name, code, user_id))
        conn.commit()

    def search(self, carID):
        # Search for username in the Users table by carID
        # conn = self.connect()
        cur = self.connection.cursor()
        cur.execute("SELECT Username FROM Users WHERE carID LIKE ?", ('%' + carID + '%',))
        results_name = cur.fetchall()
        return len(results_name) > 0,results_name

'''
table Users:
1|Alice|AB12CDE
2|Bob|XY34ZYZ
3|John|GH56HJK
4|Jack|LM78NOP
5|Sam|QR90STU
test
'''

# test
#db_manager = DataBaseManager()
#db_manager.connect()

##test add
#db_manager.add('aa', '123456')
#db_manager.add('test', 'xxxxxx')

##test search
#usera = db_manager.search('QR90STU') 
#print(usera)

##test delete
#db_manager.delete('123456')
