from dataclasses import dataclass

import datetime as datetime


@dataclass
class EnvironmentalVariable:
    """Class for keeping track of an environmental variable."""
    datetime: datetime
    temperature: float
    humidity: float
