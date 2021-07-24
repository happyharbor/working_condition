import csv

from dto.settings import Settings
from dto.work_setting import WorkSetting
from dto.work_type import WorkType


def get_settings(path='../csvs/settings.csv'):
    work_settings = []
    with open(path, newline='') as csvfile:
        settings_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(settings_reader)
        for row in settings_reader:
            work_settings.append(
                WorkSetting(WorkType(int(row[0])), float(row[1]), _parse_int_column(row[2]), _parse_int_column(row[3]),
                            _parse_int_column(row[4]), _parse_int_column(row[5])))

    return Settings(work_settings)


def _parse_int_column(value):
    try:
        return int(value)
    except ValueError:
        return None
