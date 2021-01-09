from CONSTANTS import *
from z_RR_data import data_RR

# plt.style.use('bmh')
# lines = ['-', '--', '-.', ':', ]
# lines.reverse()
# markers = ['o', '+', '.', ',', '_', '*']
# markers.reverse()
algs = ['CAMS', 'Max-sum_MST']
iterations = 10
problems = 4
fig, ax = plt.subplots()

for alg in algs:
    for line_indx, line in enumerate(data_RR[alg]['times']):
        first_item = line[1]
        new_line = []
        for item in line[1:]:
            new_line.append(item - first_item)
        data_RR[alg]['times'][line_indx] = new_line

max_iterations_max_sum_mst = []
max_iterations = {}

for alg in algs:
    max_iterations[alg] = []
    lines = data_RR[alg]['times']
    for line in lines:
        max_v = 0
        for t_index, t in enumerate(line[:-1]):
            interval = line[t_index+1] - t
            if interval > max_v:
                max_v = interval
        max_iterations[alg].append(max_v)

print(f"{ttest_ind(max_iterations['Max-sum_MST'], max_iterations['CAMS'])}")

ax.bar(range(2), (
    np.average(max_iterations['Max-sum_MST']),
    np.average(max_iterations['CAMS'])
), yerr=(
    np.std(max_iterations['Max-sum_MST']),
    np.std(max_iterations['CAMS'])
))
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_ylabel('Time Of The Longest Iteration')
# ax.set_xlabel('Iterations')
plt.xticks(range(2), ('Max-sum_MST', 'CAMS'))
# ax.legend('Men')
# ax.set_xticks(iterations)
# ax.set_xlim(xmin=iterations[0], xmax=iterations[-1])
fig.tight_layout()
plt.show()