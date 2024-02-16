from abc import ABC, abstractmethod


class GateIndicator(ABC):
    def on_gate_open(self):
        pass
    
    def on_gate_close(self):
        pass
