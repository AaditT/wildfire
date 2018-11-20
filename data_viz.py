import main
import matplotlib.pyplot as plt

y_vals = []
counter = 1
while counter < 53:
    y_vals.append(counter)
    counter += 1

def barGraph():
    import matplotlib.pyplot as plt; plt.rcdefaults()
    import numpy as np



    y_pos = y_vals
    performance = experimental()

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.yticks(y_vals)
    plt.ylabel('Experimental Chance of Wildfire')
    plt.title('California County Code')

    plt.show()
barGraph()

def pieChart():

    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
