import unittest
from datetime import date
from lyftproject import Carfactory, SpindlerBattery, NubbinBattery, WilloughbyEngine, CapuletEngine, SternmanEngine, Car


class TestEngine(unittest.TestCase):
    def test_willoughby_engine_needs_service_true(self):
        engine = WilloughbyEngine(650000, 20000)
        result = engine.needs_service()
        self.assertTrue(result)  # WilloughbyEngine needs service (current mileage - last service mileage >= 60000)

    def test_willoughby_engine_needs_service_false(self):
        engine = WilloughbyEngine(45000, 20000)
        result = engine.needs_service()
        self.assertFalse(result)  # WilloughbyEngine doesn't need service (current mileage - last service mileage < 60000)

    def test_capulet_engine_needs_service_true(self):
        engine = CapuletEngine(350000, 10000)
        result = engine.needs_service()
        self.assertTrue(result)  # CapuletEngine needs service (current mileage - last service mileage >= 30000)

    def test_capulet_engine_needs_service_false(self):
        engine = CapuletEngine(25000, 10000)
        result = engine.needs_service()
        self.assertFalse(result)  # CapuletEngine doesn't need service (current mileage - last service mileage < 30000)

    def test_sternman_engine_needs_service_true(self):
        engine = SternmanEngine('on')
        result = engine.needs_service()
        self.assertTrue(result)  # SternmanEngine needs service (warning light is 'on')

    def test_sternman_engine_needs_service_false(self):
        engine = SternmanEngine('off')
        result = engine.needs_service()
        self.assertFalse(result)  # SternmanEngine doesn't need service (warning light is 'off')


class TestBattery(unittest.TestCase):
    def test_spindler_battery_needs_service_true(self):
        current_date = date(2023, 11, 1)
        last_service_date = date(2021, 11, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        result = battery.needs_service()
        self.assertTrue(result)  # SpindlerBattery needs service (difference in years >= 2)

    def test_spindler_battery_needs_service_false(self):
        current_date = date(2023, 11, 1)
        last_service_date = date(2022, 11, 1)
        battery = SpindlerBattery(current_date, last_service_date)
        result = battery.needs_service()
        self.assertFalse(result)  # SpindlerBattery doesn't need service (difference in years < 2)

    def test_nubbin_battery_needs_service_true(self):
        current_date = date(2023, 11, 1)
        last_service_date = date(2019, 11, 1)
        battery = NubbinBattery(current_date, last_service_date)
        result = battery.needs_service()
        self.assertTrue(result)  # NubbinBattery needs service (difference in years >= 4)

    def test_nubbin_battery_needs_servic_false(self):
        current_date = date(2023, 11, 1)
        last_service_date = date(2020, 11, 1)
        battery = NubbinBattery(current_date, last_service_date)
        result = battery.needs_service()
        self.assertFalse(result)  # NubbinBattery doesn't need service (difference in years < 4)


class TestCar(unittest.TestCase):
    def test_car_needs_service_true(self):
        engine = WilloughbyEngine(65000, 20000)
        battery = SpindlerBattery(date(2023, 11, 1), date(2021, 11, 1))
        car = Car(engine, battery)
        result = car.needs_service()
        self.assertTrue(result)  # Car needs service as at least one component needs service

    def test_car_needs_service_false(self):
        engine = CapuletEngine(25000, 10000)
        battery = NubbinBattery(date(2023, 11, 1), date(2020, 11, 1))
        car = Car(engine, battery)
        result = car.needs_service()
        self.assertFalse(result)  # Car doesn't need service as no component needs service


class TestCarFactory(unittest.TestCase):
    def test_create_calliope(self):
        car_factory = Carfactory()
        current_date = date(2023, 11, 1)
        last_service_date = date(2021, 11, 1)
        result = car_factory.create_calliope(current_date, last_service_date, 50000, 20000)
        self.assertTrue(result)  # calliope car needs service based on the difference in the current_mileage - last_service_mileage >= 60000, and the date

    def test_create_glissade(self):
        car_factory = Carfactory()
        current_date = date(2023, 11, 1)
        last_service_date = date(2021, 11, 1)
        result = car_factory.creat_glissade(current_date, last_service_date, 30000, 10000)
        self.assertTrue(result)  # glissade car needs service based on the difference in the current_mileage - last_service_mileage >= 60000, and the date

    def test_create_palindrome(self):
        car_factory = Carfactory()
        current_date = date(2023, 11, 1)
        last_service_date = date(2020, 11, 1)
        result = car_factory.creat_palindrome(current_date, last_service_date, False)
        self.assertTrue(result)  # palindrome car needs service based on the difference in the current_date and last_service_date exceeded 2 years

    def test_create_rorschach(self):
        car_factory = Carfactory()
        current_date = date(2023, 11, 1)
        last_service_date = date(2021, 11, 1)
        result = car_factory.create_rorschach(current_date, last_service_date, 50000, 10000)
        self.assertFalse(result)  # rorschach car does not need service based on the difference in the current_date and last_service_date did not exceed 4 years

    def test_create_thovex(self):
        car_factory = Carfactory()
        current_date = date(2023, 11, 1)
        last_service_date = date(2021, 11, 1)
        result = car_factory.create_thovex(current_date, last_service_date, 30000, 10000)
        self.assertTrue(result)  # thovex car needs service based on the difference in the current_date and last_service_date is exaltly 2 years


if __name__ == '__main__':
    unittest.main()
