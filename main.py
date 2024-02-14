import gate_app
import gate
import mock_vehicle_id_reader
import db_manager
import vehicle_id_reader
import sys

gate = gate.Gate()
reader = mock_vehicle_id_reader.MockVehicleIdReader()
db_manger = db_manager.DataBaseManager()
app = gate_app.GateApp(gate, reader, db_manger)
try:
    app.run()
# initial and import indicator
except KeyboardInterrupt:
    print('Caught Ctrl+C, exiting gracefully')
    app.exit()
    
    sys.exit(0)