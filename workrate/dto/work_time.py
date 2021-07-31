from dataclasses import dataclass

import datetime as datetime

from workrate.dto.work_condition import WorkCondition


@dataclass
class WorkTime:
    """Class for keeping the work time."""
    datetime: datetime
    work_condition: WorkCondition
