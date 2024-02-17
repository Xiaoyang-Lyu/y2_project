import db_manager

class Menu():
    def __init__(self, db: db_manager.DataBaseManager):
        self.db = db
        pass
    
    
    def run(self):
        pass

    def change_state(self):
        pass
    


class MainMenu(Menu):
    def run(self):
        print(f"Welcome to DataBase User Interface! Please input ")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Option 5")
        print("0. Exit")

        user_input = input("Please enter your choice (0-5): ")

        if user_input == '1':
            self.option_1()
        elif user_input == '2':
            self.option_2()
        elif user_input == '3':
            self.option_3()
        elif user_input == '4':
            self.option_4()
        elif user_input == '5':
            self.option_5()
        elif user_input == '0':
            print("Exiting the program.")
            exit()
        else:
            print("Invalid choice. Please enter a number between 0 and 5.")
            return

    def option_1(self):
        print("You chose Option 1.")
        # Add your code for Option 1 here

    def option_2(self):
        print("You chose Option 2.")
        # Add your code for Option 2 here

    def option_3(self):
        print("You chose Option 3.")
        # Add your code for Option 3 here

    def option_4(self):
        print("You chose Option 4.")
        # Add your code for Option 4 here

    def option_5(self):
        print("You chose Option 5.")
        # Add your code for Option 5 here
    pass


class AddMenu(Menu):
    def run(self):
        pass

if __name__ == "__main__":
    
    menu = MainMenu(db = db_manager.DataBaseManager())
    menu.run()
