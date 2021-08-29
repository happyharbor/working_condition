import csv
import datetime

from getmetrics.dto.environmental_variable import EnvironmentalVariable


def get_reading(path='../resources/input.csv'):
    environmental_variables = []
    with open(path, newline='') as csvfile:
        environment_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(environment_reader)

        for row in environment_reader:
            date_time_str = row[0] + ' ' + row[1]
            date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%y %H:%M')
            environmental_variables.append(EnvironmentalVariable(date_time_obj, float(row[2]), float(row[3])))
    return environmental_variables
