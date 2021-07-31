from workrate.dto.work_condition import WorkCondition
from workrate.dto.work_time import WorkTime
from workrate.dto.work_type import WorkType
from workrate.readers.environment_reader import get_readings
from workrate.readers.settings_reader import get_settings


def calculate_workrate():
    settings = get_settings('workrate/resources/settings.csv')

    work_times = []
    for reading in get_readings('workrate/resources/input.csv'):
        for work_type in WorkType:
            condition = __find_work_condition(settings, work_type, reading.temperature, reading.humidity)
            work_times.append(WorkTime(reading.datetime, condition))
    print(work_times)


def __find_work_condition(settings, work_type, temperature, humidity):
    if temperature < settings.min_temperature:
        return WorkCondition.CONTINUOUS
    if temperature > settings.max_temperature:
        return WorkCondition.NO_WORK

    same_work_type = [x for x in settings.work_settings if x.work_type == work_type]
    same_temperature = [x for x in same_work_type if x.temperature == int(temperature)]

    if not len(same_temperature) == 1:
        return None

    setting = same_temperature[0]
    if (setting.continuous_work is not None) and (humidity <= setting.continuous_work):
        return WorkCondition.CONTINUOUS
    elif (setting.quarter_break is not None) and (humidity < setting.quarter_break):
        return WorkCondition.QUARTER_BREAK
    elif (setting.half_break is not None) and (humidity < setting.half_break):
        return WorkCondition.HALF_BREAK
    elif (setting.quarter_work is not None) and (humidity < setting.quarter_work):
        return WorkCondition.QUARTER_WORK
    elif (setting.quarter_work is not None) and (humidity >= setting.quarter_work):
        return WorkCondition.NO_WORK
    else:
        return None


if __name__ == "__main__":
    calculate_workrate()
