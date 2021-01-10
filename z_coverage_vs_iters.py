from CONSTANTS import *


folder_str = '04.01.2021-14:51:00_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_'
# folder_str = '06.01.2021-20:17:14_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_col-v2_'
graph_file_name = 'data/' + folder_str + '/file.graf'

folder_str2 = '04.01.2021-03:03:42_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_delay_100'
# folder_str2 = '08.01.2021-21:15:51_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_col-v2_delay-v2_100'
graph_file_name2 = 'data/' + folder_str2 + '/file.graf'

graph_file_name = graph_file_name[:-5] + '.graf'
with open(graph_file_name, 'rb') as fileObject:
    # load the object from the file into var b
    graphs100nd = pickle.load(fileObject)

graph_file_name2 = graph_file_name2[:-5] + '.graf'
with open(graph_file_name2, 'rb') as fileObject:
    # load the object from the file into var b
    graphs100d = pickle.load(fileObject)


plt.style.use('bmh')
lines = ['-', '--', '-.', ':', ]
lines.reverse()
markers = ['o', '+', '.', ',', '_', '*']
markers.reverse()
marker_index, line_index = 0, 0
# num_of_iterations, num_of_problems = graphs[algorithms[0]].shape
# t_value = t.ppf(1 - alpha, df=(NUMBER_OF_PROBLEMS - 1))
l = len(graphs100nd[list(graphs100nd.keys())[0]])
iterations = [i + 1 for i in range(len(graphs100nd[list(graphs100nd.keys())[0]]))]
# avr = np.average(a, 1)
# std = np.std(a, 1)

fig, ax = plt.subplots()


# ------------ ADD ------------ #
def add_graph(line_index, marker_index, graph_dict, alg_name, alg_label, color):
    line_index = 0 if line_index == len(lines) else line_index
    marker_index = 0 if marker_index == len(markers) else marker_index
    matrix = graph_dict[alg_name]
    avr = np.average(matrix, 1)
    std = np.std(matrix, 1)
    line = lines[line_index]
    marker = markers[marker_index]
    print(f'{alg_name}: li:{line_index} mi:{marker_index}')
    ax.plot(range(len(avr)), avr, '%s%s' % (marker, line), label=alg_label, color=color)

    ax.fill_between(range(len(avr)), avr - AMOUNT_OF_STD * std, avr + AMOUNT_OF_STD * std,
                    alpha=0.2, antialiased=True, color=color)
# ----------------------------- #

add_graph(0, 0, graphs100nd, 'Random-Walk', 'Random-Walk', 'b')

add_graph(2, 2, graphs100d, 'Max-sum_MST', 'Max-sum_MST\n(including breakdowns)', 'tab:orange')

add_graph(3, 3, graphs100nd, 'CAMS', 'CAMS', 'm')

add_graph(0, 4, graphs100nd, 'Max-sum_MST', 'Max-sum_MST', 'g')



# ax.legend(loc='upper right')
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', prop={'size': 15})
# ax.set_title('Results')
ax.set_ylabel('Remaining Coverage Requirement')
ax.set_xlabel('Iterations')
# ax.set_xticks(iterations)
# ax.set_xlim(xmin=iterations[0], xmax=iterations[-1])
fig.tight_layout()
plt.show()

