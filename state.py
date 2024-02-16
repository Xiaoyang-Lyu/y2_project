import gate
import lcd
import motor

MOTOR = 0
LCD = 1
# define a state interface 
class State:
    def __init__(self, gate):
        self.gate = gate
        pass


    def run(self):
        # the state method will be implemented here with gate
        pass

    def change_state(self):
        pass
    
    # print current_state
    def current_state(self):
        pass


class OpenState(State):
    def __init__(self, gate):
        super().__init__(gate)
        pass

    def run(self):
        # use loop to get indicator function
        # for i in self.gate._indicators:
        #     self.gate._indicators[i].on_gate_open()
        self.gate.indicator[MOTOR].on_gate_open()
        self.gate.indicator[LCD].lcd_display_string(f"Welcome!",1)
        self.gate.indicator[LCD].lcd_display_string(f"{self.gate.current_vehicle_id}",2)
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
        # use loop to get indicator function
        # for i in self.gate._indicators:
        #     self.gate._indicators[i].on_gate_close()
        self.gate.indicator[MOTOR].on_gate_close()
        self.gate.indicator[LCD].lcd_display_string(f"test",1)
        self.gate.indicator[LCD].lcd_display_string(f"test",2)
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

