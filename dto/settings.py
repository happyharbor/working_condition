from dataclasses import dataclass
from dto.work_setting import WorkSetting


@dataclass
class Settings:
    """Class for keeping the settings."""
    work_settings: list[WorkSetting]
