import menu
import db_manager

class DataBaseUIApp:
    def __init__(self):
        self.db = db_manager.DataBaseManager()
        self.menu = menu.MainMenu(self.db)

    def run(self):
        while(True):
           self.menu.run()
           self.menu = self.menu.change_state()
        pass


    def exit(self):
        pass
