import gate
import lcd
import motor

# Define magic number
CLOSED_STATE = "gate closed"
OPEN_STATE = "gate open"

# Define a state interface 
class State:
    def __init__(self, gate):
        self.gate = gate
        pass


    def run(self):
        # The state method will be implemented here with gate
        pass

    def change_state(self):
        pass
    
    # Print current_state
    def current_state(self):
        pass


class OpenState(State):
    def __init__(self, gate):
        super().__init__(gate)
        pass

    def run(self):
        # Run motor
        self.gate.motor.on_gate_open()

        # TODO: check if need print name on lcd
        # Run lcd screen
        self.gate.lcd.lcd_clear() # Clean the screen
        self.gate.lcd.lcd_display_string(f"Welcome!",1)
        self.gate.lcd.lcd_display_string(f"{self.gate.current_vehicle_id}",2)
        print("open state")


        pass

    def change_state(self):
        self.gate.state = ClosedState(self.gate)
    
    def current_state(self):
        return "gate open"
        

class ClosedState(State):
    def __init__(self, gate):
        super().__init__(gate)
        pass

    def run(self):
        # Run motor
        self.gate.motor.on_gate_close()

        # TODO: check closed state lcd output
        # Run lcd screen
        self.gate.lcd.lcd_clear() # Clean the screen
        self.gate.lcd.lcd_display_string(f"test",1)
        self.gate.lcd.lcd_display_string(f"test",2)
        print("closed state")
        
        pass

    def change_state(self):
        self.gate.state = OpenState(self.gate)

    def current_state(self):
        return "gate closed"

if __name__ == "__main__":
    gate = gate.Gate()
    print(gate.state.current_state())
    gate.state.change_state()
    print(gate.state.current_state())

