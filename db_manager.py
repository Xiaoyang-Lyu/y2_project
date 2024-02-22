import sqlite3
import re

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
        if not re.match(r'^[A-Z0-9]{7}$', carID):
            print("carID must be a 7-character alphanumeric combination.")
            return False
        
        try:
            conn = self.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO Users (Username, carID) VALUES (?, ?)", (Username, carID))
            conn.commit()
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return False  # Return False if a UNIQUE constraint violation occurs
        
    def delete(self, carID):
        # Delete a user from the Users table by carID
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("DELETE FROM Users WHERE carID = ?", (carID,))
        conn.commit()


    
    def modify(self, old_carID, Username, new_carID):
        # Modify an existing user's name and carID in the Users table by the old carID
        if not re.match(r'^[A-Z0-9]{7}$', new_carID):
            print("carID must be a 7-character alphanumeric combination.")
            return False

        try:
            conn = self.connect()
            cur = conn.cursor()
            # Update the record based on the old carID
            cur.execute("UPDATE Users SET Username = ?, carID = ? WHERE carID = ?", (Username, new_carID, old_carID))
            conn.commit()
            if cur.rowcount == 0:
                print("No user found with the specified carID.")
                return False  # Return False if no user is found with the specified carID
            return True  # Return True to indicate success
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        return False  # Return False if a UNIQUE constraint violation occurs or other database error occurs


    def search(self, carID):
        # Search for username in the Users table by carID
        # conn = self.connect()
        cur = self.connection.cursor()
        # conn = self.connect()
        cur = self.connection.cursor()
        cur.execute("SELECT Username FROM Users WHERE carID LIKE ?", ('%' + carID + '%',))
        results_name = cur.fetchall()
        return len(results_name) > 0,results_name
    
    def show_table(self):
        # Show table Users 
        conn = self.connect()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        
'''

table rule:
    CREATE TABLE Users (
    UserId INTEGER PRIMARY KEY,
    Username TEXT NOT NULL,
    carID TEXT NOT NULL UNIQUE
    );

table Users:
1|Alice|AB12CDE
2|Bob|XY34ZYZ
3|John|GH55HJK
4|Jack|LM78NOP
5|Sam|QR90STU
'''

# test
#db_manager = DataBaseManager()
#db_manager.connect()

## show table
#db_manager.show_table()

## test search
#usera = db_manager.search('QR90STU') 
#print(usera[1])
#print(usera[0])

## test add
#a = db_manager.add('a4', 'ACB4567')
#print(a)


## test modify
#db_manager.modify('3', 'john', 'GH55HJK')

## test delete
#db_manager.delete_n('a2')

