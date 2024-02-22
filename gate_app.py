from signal import pause
import gate
import db_manager
import vehicle_id_reader
import time
import motor
import lcd

# Define magic number
CLOSED_STATE = "gate closed"
OPEN_STATE = "gate open"
ISPASSED = 0
RESULTNAME = 1


class GateApp:
    def __init__(self, gate: gate.Gate, reader: vehicle_id_reader.VehicleIdReader, db_manager: db_manager.DataBaseManager):
        self.gate = gate
        self.reader = reader
        self.db_manager = db_manager

    def run(self):
        # TODO: Here could add lcd controler
        # Connect to the Database and active camera
        self.db_manager.connect()
        self.reader.active_camera()
        
        while (True):
            # Get camera output
            vehicle_id = self.reader.get_vehicle_id()
            search_results = self.db_manager.search(vehicle_id)

            # If the vehicle id got match to the id in DB, change gate state and run
            is_passed = search_results[ISPASSED]
            # TODO: result_name = search_results[RESULTNAME]

            if is_passed:
                # If gate is already open, then it doesn't run the indicators again
                if self.gate.state.current_state() == OPEN_STATE:
                    continue
                self.gate.current_vehicle_id = vehicle_id
                # TODO: self.gate.current_vehicle_name = result_name

                # Switch to open state and run the indicators
                self.gate.state.change_state()
                self.gate.state.run()
                time.sleep(8)

            else:
                # If gate is already closed, then it doesn't run the indicators again
                if self.gate.state.current_state() == CLOSED_STATE:
                    continue

                # Switch to closed state and run the indicators
                self.gate.state.change_state()
                self.gate.state.run()
                time.sleep(5)

    def exit(self):
        #Closed camera and db
        self.reader.release_camera()
        self.db_manager.close()

        if self.gate.state.current_state() == OPEN_STATE:
            self.gate.state.change_state()
            self.gate.state.run()



