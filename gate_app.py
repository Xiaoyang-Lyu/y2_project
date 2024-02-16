from signal import pause
import gate
import db_manager
import vehicle_id_reader
import time
import motor
import lcd

CLOSED_STATE = "gate closed"
OPEN_STATE = "gate open"


class GateApp:
    def __init__(self, gate: gate.Gate, reader: vehicle_id_reader.VehicleIdReader, db_manager: db_manager.DataBaseManager):
        self.gate = gate
        self.reader = reader
        self.db_manager = db_manager

    def run(self):
        # TODO: active the camera and connect to the DB
        self.db_manager.connect()
        self.reader.active_camera()

        # TODO: import real indicator
        # self.gate.register_indicator(motor.DoorIndicator)
        # self.gate.register_indicator(lcd.lcd)
        
        while (True):
            vehicle_id = self.reader.get_vehicle_id()
            # If the vehicle id got match to the id in DB, change gate state and run
            # TODO: delete test code
            is_passed = self.db_manager.search(vehicle_id)[0]
            if is_passed:
            # if self.gate.test_code == 0:
                if self.gate.state.current_state() == OPEN_STATE:
                    continue
                self.gate.current_vehicle_id = vehicle_id
                self.gate.state.change_state()
                self.gate.state.run()
                time.sleep(8)
            # TODO: delete test code
                # self.gate.test_code = 1
# TODO: Check if it need pause
            else:
                if self.gate.state.current_state() == CLOSED_STATE:
                    continue
                self.gate.state.change_state()
                self.gate.state.run()
                time.sleep(5)
            # TODO: delete test code
                # self.gate.test_code = 0
# TODO: Check if it need pause

    def exit(self):
        #TODO: closed camera and db
        self.reader.release_camera()
        self.db_manager.close()
        if self.gate.state.current_state() == OPEN_STATE:
            self.gate.state.change_state()
            self.gate.state.run()



