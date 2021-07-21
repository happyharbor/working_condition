from dto.work_condition import WorkCondition
from dto.work_type import WorkType
from readers.environment_reader import get_readings
from readers.settings_reader import get_settings


def main():
    work_settings = get_settings('csvs/settings.csv')

    work_conditions = []
    for reading in get_readings('csvs/input.csv'):
        work_conditions.append(find_work_condition(work_settings, WorkType.LIGHT, reading.temperature, reading.humidity))


def find_work_condition(settings, work_type, temperature, humidity):
    same_work_type = [x for x in settings if x.work_type == work_type]
    same_temperature = [x for x in same_work_type if x.temperature == int(temperature)]
    if not len(same_temperature) == 1:
        return None
    setting = same_temperature[0]
    if humidity <= setting.continuous_work:
        return WorkCondition.CONTINUOUS
    elif humidity <= setting.quarter_break:
        return WorkCondition.QUARTER_BREAK
    elif humidity <= setting.half_break:
        return WorkCondition.HALF_BREAK
    elif humidity <= setting.quarter_work:
        return WorkCondition.QUARTER_WORK
    elif humidity > setting.quarter_work:
        return WorkCondition.NO_WORK
    else:
        return None


if __name__ == "__main__":
    main()
