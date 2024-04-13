from abc import ABC

# Importing the Car and ServiceStrategy classes (assuming they're defined elsewhere)
from car import Car
from service_strategy import ServiceStrategy

# Concrete Warning Light Service Strategy
class WarningLightServiceStrategy(ServiceStrategy):
    def __init__(self, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def should_be_serviced(self):
        return self.warning_light_is_on

# Refactored SternmanEngine Class
class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.service_strategy = WarningLightServiceStrategy(warning_light_is_on)

    def engine_should_be_serviced(self):
        return self.service_strategy.should_be_serviced()
