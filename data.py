import matplotlib.pyplot as plt
import csv
import numpy
import pandas
from math import ceil

cols = ['UNIT', 'Total','Arson','Campfire','DebrisBurning','Elec.Power','Equip.Use','Ltng.','Misc.','P-W-F','Railroad','Smoking','Undet.','Vehicle']
csv_data_2016 = pandas.read_csv('csv/2016_data.csv', names=cols)
csv_data_2015 = pandas.read_csv('csv/2015_data.csv', names=cols)
csv_data_2014 = pandas.read_csv('csv/2014_data.csv', names=cols)

def extractData(csv_data):
    fires_array = []
    fires_dict  = {}
    totalFires = 0
    x = 1
    for index, row in csv_data.iterrows():
        unit_total = int(str(row['Total']).replace(',', ''))
        totalFires += int(unit_total)
        fires_array.append(unit_total)
        fires_dict[str(row['UNIT'])] = unit_total
    return [fires_array, totalFires, fires_dict]

def getRisk(csv_data):
    risk_by_unit = []
    fires_by_unit = extractData(csv_data)[0]
    totalFires = extractData(csv_data)[1]
    for fire_in_unit in fires_by_unit:
        fire_risk = ((100 * fire_in_unit) / (totalFires))
        risk_by_unit.append(round(fire_risk, 3))
    return risk_by_unit

def barGraph(years, *csv_data_list):
    unit_list = list(extractData(csv_data_2014)[2].keys())
    unit_list.insert(0, '')
    width=0.2
    i = 1
    x_vals = [x for x in range(1, 22)]
    for csv_data in csv_data_list:
        plt.bar(x_vals, getRisk(csv_data), alpha=0.5, color=list(plt.rcParams['axes.prop_cycle'])[i]['color'], width=width)
        x_vals = [(val + width) for val in x_vals]
        i += 1
    plt.xticks(numpy.arange(1, 22, step=1))
    plt.xticks(numpy.arange(22), unit_list, rotation=90)
    plt.ylabel('EXPERIMENTAL CHANCE OF WILDFIRE (%)')
    plt.title('FIRE RISK FOR ALL CAL FIRE UNITS FROM ' + years)
    plt.show()

barGraph('2014-2016', csv_data_2014, csv_data_2015, csv_data_2016)
