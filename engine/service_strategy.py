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

# Concrete Warning Light Service Strategy
class WarningLightServiceStrategy(ServiceStrategy):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def should_be_serviced(self):
        return self.warning_light_is_on
