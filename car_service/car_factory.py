from datetime import date

from capulet_engine import CapuletEngine
from willoughby_engine import WilloughbyEngine
from sternman_engine import SternmanEngine

from spindler_battery import SpindlerBattery
from nubbin_battery import NubbinBattery
from car import Car


class Carfactory:
    def create_calliope(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery).needs_service()

    def create_glissade(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery).needs_service()

    def create_palindrome(self,current_date:date, last_service_date:date, warning_light_on:bool):
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery).needs_service()
    

    def create_rorschach(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):
        engine = WilloughbyEngine(last_service_mileage,current_mileage)
        battery = NubbinBattery(last_service_date,current_date)
        return Car(engine,battery).needs_service()
    

    def create_thovex(self,current_date:date, last_service_date:date, current_mileage:int, last_service_mileage:int):
        engine = CapuletEngine(last_service_mileage,current_mileage)
        battery = SpindlerBattery(last_service_date,current_date)
        return Car(engine,battery).needs_service()



# current_date = date.today()
# last_date = current_date.replace(year=current_date.year - 4)

# cars = Carfactory()
# carglis= cars.create_glissade(current_date,last_date,300,40)

# carpalind = cars.create_palindrome(current_date,last_date, False)
# print(carglis)
# print(carpalind)
# print(current_date,last_date)
