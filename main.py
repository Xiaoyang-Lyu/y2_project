import gate_app
import gate
import db_manager
import vehicle_id_reader
import sys
import lcd
import motor

# Initial specific indicator 
lcd_indicator = lcd.lcd()
motor_indicator = motor.DoorIndicator()

# Initial gate
gate = gate.Gate(lcd_indicator, motor_indicator)


# Initial specific reader and DataBase manager
# Mock vehicle id reader can be used to project test without camera
# reader = vehicle_id_reader.MockVehicleIdReader()
reader = vehicle_id_reader.WebCamVehicleIdreader()
db_manger = db_manager.DataBaseManager()

# Initial gate app
app = gate_app.GateApp(gate, reader, db_manger)


try:
    # Run the whole program
    app.run()

# when catch keyboard interrupt
except KeyboardInterrupt:
    print('Caught Ctrl+C, exiting gracefully')
    # Run the quit function
    app.exit()

    # Quit program
    sys.exit(0)
