import state

class Gate:
    def __init__(self):
        # delete test code
        self.test_code = 0
        self.state = state.ClosedState(self)
        self._indicators = []
        # 
        self.current_vehicle_id = None

    def register_indicator(self, gate_indicator):
        self._indicators.append(gate_indicator)
        # TODO: delete this
        print("success add a new indicator")

    
        