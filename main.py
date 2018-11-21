import matplotlib.pyplot as plt
import csv
import numpy
import pandas
from math import ceil

cols = ['COUNTY', 'Total','Arson','Campfire','DebrisBurning','Elec.Power','Equip.Use','Ltng.','Misc.','P-W-F','Railroad','Smoking','Undet.','Vehicle']
csv_data_2016 = pandas.read_csv('csv/2016_data.csv', names=cols)
csv_data_2015 = pandas.read_csv('csv/2015_data.csv', names=cols)

def extractData(csv_data):
    fires_array = []
    fires_dict  = {}
    totalFires = 0
    x = 1
    for index, row in csv_data.iterrows():
        county_total = int(str(row['Total']).replace(',', ''))
        totalFires += int(county_total)
        fires_array.append(county_total)
        fires_dict[str(row['COUNTY'])] = county_total
    return [fires_array, totalFires, fires_dict]

def experimental(csv_data):
    risk_by_county = []
    fires_by_county = extractData(csv_data)[0]
    totalFires = extractData(csv_data)[1]
    for fire_in_county in fires_by_county:
        fire_risk = ((100 * fire_in_county) / (totalFires))
        risk_by_county.append(round(fire_risk, 3))
    return risk_by_county
