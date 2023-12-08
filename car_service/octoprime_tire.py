from serviceable import Tire

class OctoprimeTire(Tire):
    def __init__(self, wear_values) -> None:
        self.wear_values = wear_values

    def needs_service(self):
       return sum(self.wear_values) >= 3