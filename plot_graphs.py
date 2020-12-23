from CONSTANTS import *
from main_help_functions import *

# ---------------------------
# ------INPUT SETTINGS-------
# ---------------------------
graph_file_name = "data/23.12.2020-13:16:48__random_walk__harels_algorithm__max_sum_cells/_file.graf"
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













