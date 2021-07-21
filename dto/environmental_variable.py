from dataclasses import dataclass


@dataclass
class EnvironmentalVariable:
    """Class for keeping track of an environmental variable."""
    # datetime: datetime
    temperature: float
    humidity: float

    def total_cost(self) -> float:
        return self.temperature * self.humidity
