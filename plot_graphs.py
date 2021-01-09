from CONSTANTS import *
from main_help_functions import *

# ---------------------------
# ------INPUT SETTINGS-------
# ---------------------------
folder_str = '06.01.2021-20:17:14_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_col-v2_'
# folder_str = '05.01.2021-23:35:28_50Grid-_20T-80R_100Bi-30Si_50PRBLMS_delay-v2_100'
graph_file_name = 'data/' + folder_str + '/file.graf'
# graph_file_name = "data/30.12.2020-13:11:35_50Grid-_20T-80R_40Bi-30Si_targets_apart_/file.graf"
# need_to_plot_variance = False
# need_to_plot_min_max = False
# ---------------------------

graph_file_name = graph_file_name[:-5] + '.info'
with open(graph_file_name, 'rb') as fileObject:
    # load the object from the file into var b
    info = pickle.load(fileObject)
    # pprint(info['collisions'])
    # for k, v in info['collisions'].items():
    #     print(k, 'collisions mean: ', (statistics.mean(v)/2), 'std:', (statistics.stdev(v)/2))
    pprint(info)


graph_file_name = graph_file_name[:-5] + '.graf'
with open(graph_file_name, 'rb') as fileObject:
    # load the object from the file into var b
    graphs = pickle.load(fileObject)
    algorithms = list(graphs.keys())
    plot_results_if(graphs)
    print_t_test(graphs)


graph_file_name = graph_file_name[:-5] + '.resu'
with open(graph_file_name, 'rb') as fileObject:
    # load the object from the file into var b
    results_dict = pickle.load(fileObject)
    plot_collisions(results_dict)

# '.'
# ','
# 'o'
# 'v'
# '^'
# '<'
# '>'
# '1'
# '2'
# '3'
# '4'
# 's'
# 'p'
# '*'
# 'h'
# 'H'
# '+'
# 'x'
# 'D'
# 'd'
# '|'
# '_'













