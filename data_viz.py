import main
import matplotlib.pyplot as plt

y_vals = []
counter = 1
while counter < 53:
    y_vals.append(counter)
    counter += 1

counties_with_fires = []

def barGraph():
    plt.bar(y_vals, main.experimental(), align='center', alpha=0.5, color='r', width=0.8)
    plt.xticks([1,2,35, 42])
    plt.ylabel('Experimental Chance of Wildfire')
    plt.title('California County Code')
    plt.show()

barGraph()
