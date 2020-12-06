from CONSTANTS import *


def load_weight_of(agent_name: str, file_to_load_name: str):
    with open(file_to_load_name, 'rb') as handle:
        return pickle.load(handle)[agent_name]


def flatten_message(message):
    min_value = 99999
    for v in message.values():
        min_value = min(min_value, v)

    for k in message.keys():
        message[k] = message[k] - min_value


def get_random_num():
    return random.choice(range(1000)) / 1000


def distance(pos1, pos2):
    """
    input:
    output:
    """
    return math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))


def in_area(pos_1, pos_2, curr_SR):
    """
    input:
    output:
    """
    px, py = pos_1
    tx, ty = pos_2
    return math.sqrt(math.pow(px - tx, 2) + math.pow(py - ty, 2)) < curr_SR


def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
    curr_ang = ang + 360 if ang < 0 else ang
    small_ang = 360 - curr_ang if curr_ang > 180 else curr_ang
    return small_ang


def calc_collisions(new_positions):
    col = 0
    for robot_name_1, pos_1 in new_positions.items():
        for robot_name_2, pos_2 in new_positions.items():
            if robot_name_1 != robot_name_2 and distance(pos_1, pos_2) == 0:
                col += 1
    return col


def separate_all_agents(all_agents):
    robots = []
    targets = []
    cells = []
    robots_dict = {}
    cells_dict = {}
    for agent in all_agents:
        if 'robot' in agent.name:
            robots.append(agent)
            robots_dict[agent.name] = agent
        elif 'target' in agent.name:
            targets.append(agent)
        elif 'cell' in agent.name:
            cells.append(agent)
            cells_dict[agent.num] = agent
        else:
            raise RuntimeError('[ERROR]: unknown agent')
    return robots, targets, cells, robots_dict, cells_dict


def print_iteration_in_smaller_loop(iteration):
    print(f'\rIteration in a smaller loop: {iteration + 1}', end='')
    if iteration == ITERATIONS_IN_SMALL_LOOPS-1:
        print()