import csv

from workrate.dto.settings import Settings
from workrate.dto.work_setting import WorkSetting
from workrate.dto.work_type import WorkType


def get_settings(path='../resources/settings.csv'):
    work_settings = []
    with open(path, newline='') as csvfile:
        settings_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(settings_reader)
        for row in settings_reader:
            work_settings.append(
                WorkSetting(WorkType(int(row[0])), float(row[1]), __parse_int_column(row[2]), __parse_int_column(row[3]),
                            __parse_int_column(row[4]), __parse_int_column(row[5])))

    return Settings(work_settings)


def __parse_int_column(value):
    try:
        return int(value)
    except ValueError:
        return None
