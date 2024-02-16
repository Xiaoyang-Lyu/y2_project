import gate_app
import gate
import db_manager
import vehicle_id_reader
import sys


gate = gate.Gate()
# reader = vehicle_id_reader.MockVehicleIdReader()
reader = vehicle_id_reader.WebCamVehicleIdreader()
db_manger = db_manager.DataBaseManager()
app = gate_app.GateApp(gate, reader, db_manger)
try:
    app.run()
# initial and import indicator
except KeyboardInterrupt:
    print('Caught Ctrl+C, exiting gracefully')
    app.exit()
    
    sys.exit(0)

# test code 
# try:
#     while(True):
#         time.sleep(1)
    
# except KeyboardInterrupt:
#     print('Caught Ctrl+C, exiting gracefully')
    
#     sys.exit(0)