from abc import ABC, abstractmethod

# Define the Service Strategy Interface
class ServiceStrategy(ABC):
    @abstractmethod
    def should_be_serviced(self):
        pass

# Concrete Mileage Service Strategy
class MileageServiceStrategy(ServiceStrategy):
    def __init__(self, current_mileage, last_service_mileage, mileage_threshold):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.mileage_threshold = mileage_threshold

    def should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.mileage_threshold

# Refactored WilloughbyEngine Class
class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.service_strategy = MileageServiceStrategy(current_mileage, last_service_mileage, 60000)

    def engine_should_be_serviced(self):
        return self.service_strategy.should_be_serviced()
