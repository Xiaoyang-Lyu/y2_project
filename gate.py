import state
import motor
import lcd

class Gate:
    def __init__(self):
        # delete test code
        self.test_code = 0
        self.state = state.ClosedState(self)
        # self.indicators = []
        # 
        self.motor = motor.DoorIndicator()
        self.lcd = lcd.lcd()
        self.current_vehicle_id = None

    # def register_indicator(self, gate_indicator):
    #     self.indicators.append(gate_indicator)
    #     # TODO: delete this
    #     print("success add a new indicator")

    
        