import menu
import db_manager

class DataBaseUIApp:
    def __init__(self, menu:menu.Menu):
        self.menu = menu
        

    def run(self):
        while(True):
           self.menu.run()
           self.menu = self.menu.change_menu()
        pass


    def exit(self):
        pass

if __name__ == "__main__":
    db = db_manager.DataBaseManager()
    me = menu.MainMenu(db)
    app = DataBaseUIApp(me)
    app.run()