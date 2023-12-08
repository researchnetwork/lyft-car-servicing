from serviceable import Tire

class CarriganTire(Tire):
    def __init__(self, wear_values) -> None:
        self.wear_values = wear_values
  
    def needs_service(self):
       return any(v >= 0.9 for v in self.wear_values)