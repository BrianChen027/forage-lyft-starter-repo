from abc import ABC

# Importing the Car and ServiceStrategy classes (assuming they're defined elsewhere)
from car import Car
from .service_strategy import ServiceStrategy

# Using the existing MileageServiceStrategy but with different parameters
class MileageServiceStrategy(ServiceStrategy):
    def __init__(self, current_mileage, last_service_mileage, mileage_threshold):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.mileage_threshold = mileage_threshold

    def should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > self.mileage_threshold

# Refactored CapuletEngine Class
class CapuletEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.service_strategy = MileageServiceStrategy(current_mileage, last_service_mileage, 30000)

    def needs_service(self):
        return self.service_strategy.should_be_serviced()

