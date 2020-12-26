from CONSTANTS import *

graphs = {
    'random_walk': [2325,2319,2283,2340,2340,2328],
    'harels_algorithm': [1686,1677,1614,1716,1728,1755],
    'max_sum_cells': [1662,1728,1614,1656,1641,1665],
}

x = [5,10,30,50,70,90]

for k,v in graphs.items():

    plt.plot(x, v, label=k)

plt.xticks(x)
plt.legend()
plt.show()