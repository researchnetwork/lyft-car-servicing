from datetime import date

from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine

from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery

from octoprime_tire import OctoprimeTire
from carrigan_tire import CarriganTire

from car import Car


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
