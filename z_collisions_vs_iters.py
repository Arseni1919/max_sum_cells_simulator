from CONSTANTS import *

folder_str = '06.01.2021-20:17:14_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_col-v2_'
graph_file_name = 'data/' + folder_str + '/file.graf'

folder_str2 = '08.01.2021-21:15:51_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_col-v2_delay-v2_100'
graph_file_name2 = 'data/' + folder_str2 + '/file.graf'

graph_file_name = graph_file_name[:-5] + '.resu'
with open(graph_file_name, 'rb') as fileObject:
    # load the object from the file into var b
    results_dict100nd = pickle.load(fileObject)

graph_file_name2 = graph_file_name2[:-5] + '.resu'
with open(graph_file_name2, 'rb') as fileObject:
    # load the object from the file into var b
    results_dict100d = pickle.load(fileObject)

plt.style.use('bmh')
lines = ['-', '--', '-.', ':', ]
lines.reverse()
markers = ['o', '+', '.', ',', '_', '*']
markers.reverse()
marker_index, line_index = 0, 0
algs = ['Random-Walk', 'CAMS', 'Max-sum_MST']
iterations = 100
problems = range(50)
fig, ax = plt.subplots()

results_dict_list = [results_dict100d, results_dict100nd]

for alg_name in algs:
    for rd in results_dict_list:
        curr_col_list_yd = rd[alg_name]['col']
        chunks = [curr_col_list_yd[x:x + iterations] for x in range(0, len(curr_col_list_yd), iterations)]
        rd[alg_name] = np.array([np.cumsum(x) for x in chunks])
    print()


# ------------ ADD ------------ #
def add_graph(line_index, marker_index, graph_dict, alg_name, alg_label, color):
    line_index = 0 if line_index == len(lines) else line_index
    marker_index = 0 if marker_index == len(markers) else marker_index
    matrix = graph_dict[alg_name]
    avr = np.average(matrix, 0)
    std = np.std(matrix, 0)
    line = lines[line_index]
    marker = markers[marker_index]
    print(f'{alg_name}: li:{line_index} mi:{marker_index}')
    ax.plot(range(len(avr)), avr, '%s%s' % (marker, line), label=alg_label, color=color)

    ax.fill_between(range(len(avr)), avr - AMOUNT_OF_STD * std, avr + AMOUNT_OF_STD * std,
                    alpha=0.2, antialiased=True, color=color)


# ----------------------------- #

add_graph(0, 0, results_dict100nd, 'Random-Walk', 'Random-Walk', 'b')

add_graph(0, 4, results_dict100nd, 'Max-sum_MST', 'Max-sum_MST', 'g')

add_graph(2, 2, results_dict100d, 'Max-sum_MST', 'Max-sum_MST\n(including breakdowns)', 'tab:orange')

add_graph(3, 3, results_dict100nd, 'CAMS', 'CAMS', 'm')

# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 13})
# ax.set_title('Collisions')
ax.set_ylabel('Collisions')
ax.set_xlabel('Iterations')
# ax.set_xticks(iterations)
# ax.set_xlim(xmin=iterations[0], xmax=iterations[-1])
fig.tight_layout()
plt.show()
