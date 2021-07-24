from dataclasses import dataclass
from operator import attrgetter

from dto.work_setting import WorkSetting


@dataclass
class Settings:
    """Class for keeping the settings."""
    work_settings: list[WorkSetting]
    min_temperature: float
    max_temperature: float

    def _min(self) -> float:
        return min(self.work_settings, key=attrgetter('temperature')).temperature

    def _max(self) -> float:
        return max(self.work_settings, key=attrgetter('temperature')).temperature + 1

    def __init__(self, work_settings):
        self.work_settings = work_settings
        self.min_temperature = self._min()
        self.max_temperature = self._max()
