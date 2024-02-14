import state

class Gate:
    def __init__(self):
        self.state = state.ClosedState(self)
        self._indicators = []
        # 
        self.current_vehicle_id = None
        pass

    def register_indicator(self, gate_indicator):
        self._indicators.append(gate_indicator)
        pass

    
        