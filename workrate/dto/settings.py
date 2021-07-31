from dataclasses import dataclass
from operator import attrgetter

from workrate.dto.work_setting import WorkSetting


@dataclass
class Settings:
    """Class for keeping the settings."""
    work_settings: list[WorkSetting]
    min_temperature: float
    max_temperature: float

    def __min(self) -> float:
        return min(self.work_settings, key=attrgetter('temperature')).temperature

    def __max(self) -> float:
        return max(self.work_settings, key=attrgetter('temperature')).temperature + 1

    def __init__(self, work_settings):
        self.work_settings = work_settings
        self.min_temperature = self.__min()
        self.max_temperature = self.__max()
