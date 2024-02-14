import gate_app
import gate
import mock_vehicle_id_reader
import db_manager


gate = gate.Gate()
reader = mock_vehicle_id_reader.MockVehicleIdReader()
dbmanger = db_manager.DataBaseManager()
app = gate_app.GateApp(gate, reader, dbmanger)
# initial and import indicator

app.run()