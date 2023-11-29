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
