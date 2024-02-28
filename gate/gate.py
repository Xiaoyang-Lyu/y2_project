import gate.state as state
import indicators.motor as motor
import indicators.lcd as lcd

class Gate:
    def __init__(self, lcd: lcd.lcd, motor: motor.DoorIndicator):
        self.state = state.ClosedState(self)
        self.motor = motor
        self.lcd = lcd
        self.current_vehicle_id = None
        # TODO: self.current_vehicle_name = None


    
        