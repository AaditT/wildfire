import matplotlib.pyplot as plt
import csv
import numpy
import pandas
from math import ceil

cols = ['COUNTY', 'Total','Arson','Campfire','DebrisBurning','Elec.Power','Equip.Use','Ltng.','Misc.','P-W-F','Railroad','Smoking','Undet.','Vehicle']
csv_data = pandas.read_csv('2016_data.csv', names=cols)
print(csv_data)

def extractData():
    fires_by_county = []
    totalFires = 0
    x = 1
    for index, row in csv_data.iterrows():
        county_total = int(row['Total'].replace(',', ''))
        totalFires += int(county_total)
        fires_by_county.append(county_total)
    for x in range(0, len(fires_by_county)):
        print('County', x+1, ':', fires_by_county[x])
    print('Total Fires:', sum(fires_by_county))
    return [fires_by_county, totalFires]

def experimental():
    risk_by_county = []
    fires_by_county = extractData()[0]
    totalFires = extractData()[1]
    for fire_in_county in fires_by_county:
        fire_risk = ((100 * fire_in_county) / (totalFires))
        risk_by_county.append(round(fire_risk, 3))
    print(risk_by_county)

# data visualization
def visualize():
    pass

experimental()
