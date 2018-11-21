# Data Visualization of Fire Risk
# TODO: add comparitive bar graph
import main
import matplotlib.pyplot as plt
import pandas

cols = ['COUNTY', 'Total','Arson','Campfire','DebrisBurning','Elec.Power','Equip.Use','Ltng.','Misc.','P-W-F','Railroad','Smoking','Undet.','Vehicle']
csv_data_2016 = pandas.read_csv('csv/2016_data.csv', names=cols)
csv_data_2015 = pandas.read_csv('csv/2015_data.csv', names=cols)

# makes sure that x-values exist at each of the 52 California counties
x_vals = []
counter = 1
while counter < 55:
    x_vals.append(counter)
    counter += 1

# makes sure that x-axis has ticks at every even number to prevent overcrowding on x-axis
even_num_54 = []
even_counter = 0
while even_counter < 55:
    even_num_54.append(even_counter)
    even_counter += 2

# functions that creates the bar graph for each year accordingly
def barGraph_2015():
    plt.bar(x_vals, main.experimental(csv_data_2015), align='center', alpha=0.5, color='r', width=0.8)
    plt.xticks(even_num_54)
    plt.ylabel('Experimental Chance of Wildfire (%)')
    plt.title('California County Code (2015)')
    plt.show()

def barGraph_2016():
    plt.bar(x_vals, main.experimental(csv_data_2016), align='center', alpha=0.5, color='r', width=0.8)
    plt.xticks(even_num_54)
    plt.ylabel('Experimental Chance of Wildfire (%)')
    plt.title('California County Code (2016)')
    plt.show()

# 2015 data:
# barGraph_2015()
# 2016 data:
# barGraph_2016()
