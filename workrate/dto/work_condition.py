from enum import Enum


class WorkCondition(Enum):
    CONTINUOUS = 1
    QUARTER_BREAK = 2
    HALF_BREAK = 3
    QUARTER_WORK = 4
    NO_WORK = 5
