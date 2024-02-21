from sre_constants import SUCCESS
import db_manager
import os
import signal
import time
ADDMENU = '1'
DELETEMENU = '2'
SEARCHMENU = '3'
MODIFYMENU = '4'
MAINMENU = '5'
EXIT = '0'




class Menu():
    def __init__(self, db: db_manager.DataBaseManager):
        self.db = db
        self.db.connect()
        self.current_menu = None
        pass
    
    
    def run(self):
        pass

    def change_menu(self):
        self.db.close()
        return MainMenu(self.db)
        pass
    


class MainMenu(Menu):
        
    def run(self):
        self.current_menu = MAINMENU
        print(f"Welcome to DataBase User Interface! Please input ")
        print("1. Add")
        print("2. Delete")
        print("3. Search")
        print("4. Modify")
        print("0. Exit")

        user_input = input("Please enter your choice (0-5): ")

        if user_input == ADDMENU:
            self.current_menu = ADDMENU

        elif user_input == DELETEMENU:
            self.current_menu = DELETEMENU

        elif user_input == SEARCHMENU:
            self.current_menu = SEARCHMENU

        elif user_input == MODIFYMENU:
            self.current_menu = MODIFYMENU

        elif user_input == EXIT:
            # send KeyboardInterrupt signal
            os.kill(os.getpid(), signal.SIGINT)

        else:
            print("Invalid choice. Please enter a number between 0 and 5.")
            return
        
    def change_menu(self):
        self.db.close()
        if self.current_menu == ADDMENU:
            return AddMenu(self.db)
        
        if self.current_menu == DELETEMENU:
            return DeleteMenu(self.db)

        if self.current_menu == SEARCHMENU:
            return SearchMenu(self.db)

        if self.current_menu == MODIFYMENU:
            return ModifyMenu(self.db)


class AddMenu(Menu):
    def run(self):
        user_name_input = input("Please input your name:")
        user_vehicle_id_input = input("Please input your plate ID:")
        is_added = self.db.add(user_name_input, user_vehicle_id_input)
        if is_added:
            print("You have successfully added a user!")
        
        else:
            print("Add failed. The plate ID is already exist or the plate ID does not conform to the format!")

        self.current_menu = MAINMENU

    # def change_menu(self):
    #     return MainMenu(self.db)
            
class DeleteMenu(Menu):
    def run(self):
        user_input = input("Please input plate ID you want to delete or input a character to quit:")
        is_deleted = self.db.delete(user_input)
        if is_deleted:
            print(f"You have successfully deleted the user {user_input}")

        else:
            print("Delete failed. The plate ID is not exist or the plate does not conform to the format!")

        self.current_menu = MAINMENU

    # def change_menu(self):
    #     return MainMenu(self.db)


ISSUCCESS = 0
RESULT = 1

class SearchMenu(Menu):
    def run(self):
        user_input = input("Please input the plate ID:")
        is_success = self.db.search(user_input)[ISSUCCESS]
        if is_success:
            print(f"The result is: {self.db.search(user_input)[RESULT]} plate ID: {user_input}")

        else:
            print(f"{user_input} does not exist!")

        self.current_menu = MAINMENU

    # def change_menu(self):
    #     return MainMenu(self.db)


class ModifyMenu(Menu):
    def run(self):
        modified_id = input("Please input the plate ID:")
        is_success = self.db.search(modified_id)[ISSUCCESS]

        if is_success:
            print(f"The user is: {self.db.search(modified_id)[RESULT]} plate ID: {modified_id}")
            input_name = input("Please input new name:")
            input_id = input("Please input new ID:")
            is_success = self.db.modify(modified_id, input_name, input_id)

            if is_success:
                print("Your changed successful!")
                self.current_menu = MainMenu
                return
            else:
                print("Your changed failed. Please check the format of new id ID")
                self.current_menu = MainMenu
                return

        else: 
            print(f"{modified_id} does not exist")
        self.current_menu = MainMenu
        






if __name__ == "__main__":
    
    # menu = MainMenu(db = db_manager.DataBaseManager())
    # menu.run()

    try:
        print("Running... Press Ctrl+C to exit.")
        while True:
            # 在这里放你的程序主体逻辑
            time.sleep(1)
            os.kill(os.getpid(), signal.SIGINT)
    except KeyboardInterrupt:
        # 如果你的程序在循环之外，也可以在这里添加退出操作
        print("Received Ctrl+C. Exiting...")
        exit(0)