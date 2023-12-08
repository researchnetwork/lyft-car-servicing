from datetime import date
from abc import ABC, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self)-> bool:
        pass


class Engine(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass

class Battery(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass


class Tire(Serviceable):
    @abstractmethod
    def needs_service(self):
        pass


class Car:
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire
        

    def needs_service(self):
        return (self.engine.needs_service() or 
                self.battery.needs_service() or
                self.tire.needs_service())

    
class CarriganTire(Tire):
    def __init__(self, wear_values) -> None:
        self.wear_values = wear_values
  
    def needs_service(self):
       return any(v >= 0.9 for v in self.wear_values)


class OctoprimeTire(Tire):
    def __init__(self, wear_values) -> None:
        self.wear_values = wear_values

    def needs_service(self):
       return sum(self.wear_values) >= 3
    

class CapuletEngine(Engine):
    def __init__(self, current_mileage:int, last_service_mileage:int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage >= 30000


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage:int, last_service_mileage:int):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self):
        return (self.current_mileage - self.last_service_mileage) >= 30000


class SternmanEngine(Engine):
    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    def needs_service(self):
        return True if self.warning_light_on == 'on' else False


class SpindlerBattery(Battery):
    def __init__(self,current_date:date, last_service_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date.year - self.last_service_date.year) >= 3


class NubbinBattery(Battery):
    def __init__(self, current_date:date, last_service_date:date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        return (self.current_date.year - self.last_service_date.year) >= 4


class Carfactory:
    def create_calliope(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, wear_values:list):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTire(wear_values)
        return Car(engine,battery,tire).needs_service()

    def creat_glissade(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, wear_values:list):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = OctoprimeTire(wear_values)
        return Car(engine,battery,tire).needs_service()

    def creat_palindrome(self,current_date:date, last_service_date:date, warning_light_on:bool, wear_values):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTire(wear_values)
        return Car(engine,battery,tire).needs_service()
    
    def create_rorschach(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, wear_values):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        tire = OctoprimeTire(wear_values)
        return Car(engine,battery,tire).needs_service()
    
    def create_thovex(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int, wear_values:list):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        tire = CarriganTire(wear_values)
        return Car(engine,battery,tire).needs_service()