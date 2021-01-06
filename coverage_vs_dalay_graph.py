from CONSTANTS import *

graphs = {
    'Random-Walk': [2310, 2361, 2298, 2340, 2292, 2331],
    'Max-sum_MST': [1248, 1326, 1449, 1419, 1398, 1539],
    'CAMS': [1290, 1389, 1353, 1308, 1293, 1353],
}

x = [2, 10, 30, 50, 70, 90]
p_values_harels_vs_cells = [0.58, 0.25, 0.07, 0.14, 0.16, 0.03]
for k, v in graphs.items():
    plt.plot(x, v, label=k)

plt.xticks(x)
plt.xlabel('Delay')
plt.ylabel('Coverage')
plt.legend()
plt.show()
