import gate

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


class OpenState(State):
    def __init__(self, gate):
        super().__init__(gate)
        pass

    def run(self):
        print(1)
        pass

    def change_state(self):
        self.gate.state = ClosedState(gate)
        

class ClosedState(State):
    def __init__(self, gate):
        super().__init__(gate)
        pass

    def run(self):
        print(2)
        
        pass

    def change_state(self):
        self.gate.state = OpenState(gate)

if __name__ == "__main__":
    gate = gate.Gate()
    gate.state.run()
    gate.state.change_state()
    gate.state.run()

