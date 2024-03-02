import gate.gate_app as gate_app
import gate.gate as gate
import imdb.db_manager as db_manager
import reader.vehicle_id_reader as vehicle_id_reader
import sys
import indicators.lcd as lcd
import indicators.motor as motor

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

# When meet error, the program will release resource
finally:
    # Run the quit function
    app.exit()

    # Quit program
    sys.exit(0)
