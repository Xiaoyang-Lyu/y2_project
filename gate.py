import state

class Gate:
    def __init__(self):
        self.state = state.ClosedState(self)
        self.indicators = []

        pass

    def register_indicator(self, gate_indicator):
        self.indicators.append(gate_indicator)
        pass