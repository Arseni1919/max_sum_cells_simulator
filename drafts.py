from CONSTANTS import *
# from main_help_functions import plot_results_if, print_t_test
# file_name = 'data/try/try.txt'
# os.mkdir('data/try')
# some_str = 'hello'
# with open(file_name, 'wb') as fileObject:
#     pickle.dump(some_str, fileObject)
# pr = '_'
# pr += 'delay_%s' % 123 if False else 'noooo'
# print(pr)

folder_str = '04.01.2021-14:51:00_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_'
graph_file_name = 'data/' + folder_str + '/file.graf'

folder_str2 = '04.01.2021-03:03:42_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_delay_100'
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
markers = [',', '+', '_', '.', 'o', '*']
markers.reverse()
marker_index, line_index = 0, 0
# num_of_iterations, num_of_problems = graphs[algorithms[0]].shape
# t_value = t.ppf(1 - alpha, df=(NUMBER_OF_PROBLEMS - 1))
l = len(graphs100nd[list(graphs100nd.keys())[0]])
iterations = [i + 1 for i in range(len(graphs100nd[list(graphs100nd.keys())[0]]))]
# avr = np.average(a, 1)
# std = np.std(a, 1)

fig, ax = plt.subplots()

for alg_name in graphs100nd.keys():

    line_index = 0 if line_index == len(lines) else line_index
    marker_index = 0 if marker_index == len(markers) else marker_index

    matrix = graphs100nd[alg_name]
    avr = np.average(matrix, 1)
    print('%s last iteration: %s' % (alg_name, avr[-1]))
    std = np.std(matrix, 1)

    line = lines[line_index]
    marker = markers[marker_index]

    ax.plot(iterations, avr, '%s%s' % (marker, line), label=alg_name)

    line_index += 1
    marker_index += 1

    if NEED_TO_PLOT_VARIANCE:
        # confidence interval
        ax.fill_between(iterations, avr - AMOUNT_OF_STD * std, avr + AMOUNT_OF_STD * std,
                        alpha=0.2, antialiased=True)

    if NEED_TO_PLOT_MIN_MAX:
        # confidence interval
        ax.fill_between(iterations, np.min(matrix, 1), np.max(matrix, 1),
                        alpha=0.2, antialiased=True)

# ------------ ADD ------------ #
line_index += 1
marker_index += 1

alg_name = 'Max-sum_MST'
line_index = 0 if line_index == len(lines) else line_index
marker_index = 0 if marker_index == len(markers) else marker_index

matrix = graphs100d[alg_name]
avr = np.average(matrix, 1)
std = np.std(matrix, 1)

line = lines[line_index]
marker = markers[marker_index]

ax.plot(iterations, avr, '%s%s' % (marker, line), label=alg_name + ' (including breakdowns)')

ax.fill_between(iterations, avr - AMOUNT_OF_STD * std, avr + AMOUNT_OF_STD * std,
                alpha=0.2, antialiased=True)


# ----------------------------- #

# ax.legend(loc='upper right')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# ax.set_title('Results')
ax.set_ylabel('Coverage')
ax.set_xlabel('Iterations')
# ax.set_xticks(iterations)
# ax.set_xlim(xmin=iterations[0], xmax=iterations[-1])
fig.tight_layout()
plt.show()

