from dataclasses import dataclass
from workrate.dto.work_type import WorkType


@dataclass
class WorkSetting:
    """Class for keeping the work setting."""
    work_type: WorkType
    temperature: float
    continuous_work: int
    quarter_break: int
    half_break: int
    quarter_work: int
