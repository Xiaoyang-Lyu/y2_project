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
    
    pass


class AddMenu(Menu):
    def run(self):
        pass
