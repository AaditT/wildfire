import main
import matplotlib.pyplot as plt

fires_by_county = main.experimental()

x_vals = []
counter = 1
while counter < 53:
    x_vals.append(counter)
    counter += 1

odd_num_52 = []
odd_counter = 0
while odd_counter < 53:
    odd_num_52.append(odd_counter)
    odd_counter += 2

def barGraph():
    plt.bar(x_vals, main.experimental(), align='center', alpha=0.5, color='r', width=0.8)
    plt.xticks(odd_num_52)
    plt.ylabel('Experimental Chance of Wildfire (%)')
    plt.title('California County Code')
    plt.show()
