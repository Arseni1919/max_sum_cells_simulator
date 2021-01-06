from CONSTANTS import *


folder_str = '04.01.2021-14:51:00_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_'
graph_file_name = 'data/' + folder_str + '/file.graf'

folder_str2 = '05.01.2021-23:35:28_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_delay-v2_100'
graph_file_name2 = 'data/' + folder_str2 + '/file.graf'

graph_file_name = graph_file_name[:-5] + '.resu'
with open(graph_file_name, 'rb') as fileObject:
    # load the object from the file into var b
    results_dict100nd = pickle.load(fileObject)

graph_file_name2 = graph_file_name2[:-5] + '.resu'
with open(graph_file_name2, 'rb') as fileObject:
    # load the object from the file into var b
    results_dict100d = pickle.load(fileObject)


# results_dict[alg_name] = {'col': []}
alg_names = list(results_dict100nd.keys())
iterations = range(len(results_dict100nd[alg_names[0]]['col']))
fig, ax = plt.subplots()

for alg_name in alg_names:
    curr_col_list = results_dict100nd[alg_name]['col']
    cumsum_list = np.cumsum(curr_col_list)
    ax.plot(iterations, cumsum_list, label=alg_name)

# ------------ ADD ------------ #
alg_name = 'Max-sum_MST'
curr_col_list = results_dict100d[alg_name]['col']
cumsum_list = np.cumsum(curr_col_list)
ax.plot(iterations, cumsum_list, label=alg_name + ' (including breakdowns)')
# ----------------------------- #

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# ax.set_title('Collisions')
ax.set_ylabel('Collisions')
ax.set_xlabel('Iterations')
# ax.set_xticks(iterations)
# ax.set_xlim(xmin=iterations[0], xmax=iterations[-1])
fig.tight_layout()
plt.show()
