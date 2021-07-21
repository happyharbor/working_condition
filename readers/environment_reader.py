import csv

from dto.environmental_variable import EnvironmentalVariable


def get_readings(path='../csvs/input.csv'):
    environmental_variables = []
    with open(path, newline='') as csvfile:
        environment_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        next(environment_reader)
        for row in environment_reader:
            environmental_variables.append(EnvironmentalVariable(float(row[2]), float(row[3])))
    return environmental_variables
