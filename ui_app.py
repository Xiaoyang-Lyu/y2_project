import menu
import db_manager
import os

class DataBaseUIApp:
    def __init__(self, menu: menu.Menu, db: db_manager.DataBaseManager):
        self.menu = menu
        self.db = db        

    def run(self):
        os.system('clear')
        while(True):
           self.menu.run()
           self.menu = self.menu.change_menu()
        pass


    def exit(self):
        self.db.close()
        pass

if __name__ == "__main__":
    db = db_manager.DataBaseManager()
    # it can initial any menu
    main_menu = menu.MainMenu(db)
    app = DataBaseUIApp(main_menu, db)
    try:
        print("Running... Press Ctrl+C to exit.")
        app.run()
    except KeyboardInterrupt:
        print("Received Ctrl+C. Exiting...")
        app.exit()
        exit(0)