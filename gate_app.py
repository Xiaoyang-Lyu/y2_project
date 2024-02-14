from signal import pause
import gate
import db_manager
import vehicle_id_reader
import time

CLOSED_STATE = "closed"
OPEN_STATE = "open"


class GateApp:
    def __init__(self, gate: gate.Gate, reader: vehicle_id_reader.VehicleldReader, db_manager: db_manager.DataBaseManager):
        self.gate = gate
        self.reader = reader
        self.db_manager = db_manager

    def run(self):
        while (True):
            vehicle_id = self.reader.get_vehicle_id()
            self.gate.current_vehicle_id = vehicle_id
            # If the vehicle id got match to the id in DB, change gate state and run
            if self.db_manager.search(vehicle_id):
                if self.gate.state.current_state() == OPEN_STATE:
                    continue
                self.gate.state.change_state()
                self.gate.state.run()
# TODO: Check if it need pause
            else:
                if self.gate.state.current_state() == CLOSED_STATE:
                    continue
                self.gate.state.change_state()
                self.gate.state.run()
# TODO: Check if it need pause

    def exit(self):
        if self.gate.state.current_state() == OPEN_STATE:
            self.gate.state.change_state()
            self.gate.state.run()

# TODO: test code