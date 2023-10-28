from abc import ABC, abstractmethod

class ServiceA(ABC):
    @abstractmethod
    def execute(self):
        pass

class ServiceAImpl1(ServiceA):
    def execute(self):
        return "Running from service A - 1"

class ServiceAImpl2(ServiceA):
    def execute(self):
        return "Running from service A - 2"

class ServiceB(ABC):
    @abstractmethod
    def run(self):
        pass

class ServiceBImpl1(ServiceB):
    def run(self):
        return "Running from service B - 1"

class ServiceBImpl2(ServiceB):
    def run(self):
        return "Running from service B - 2"


