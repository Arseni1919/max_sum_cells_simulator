from CONSTANTS import *
from pure_functions import *
from select_pos import select_pos


def DSA_MST(params, all_agents):
    robots, targets, cells, robots_dict, cells_dict = separate_all_agents(all_agents)
    clear_domains_and_neighbours_update_runds_update_cells(all_agents, robots, targets, cells)
    set_robots_domains_and_neighbours_for_robots_and_cells(robots, cells)
    # send_message - v
    # possible_pos - v
    new_positions = get_new_positions(robots_dict, cells_dict, targets)
    new_positions = analyze_and_correct_new_positions(new_positions, robots_dict)
    collisions = calc_collisions(new_positions)
    return new_positions, collisions


def clear_domains_and_neighbours_update_runds_update_cells(all_agents, robots, targets, cells):
    for agent in all_agents:
        agent.neighbours = []
        if LOAD_PREVIOUS_WEIGHTS:
            agent.rund = load_weight_of(agent.name, FILE_NAME)['rund']
        else:
            agent.update_rund()
    for robot in robots:
        robot.domain = []
        # robot.prev_pos = robot.pos
    for cell in cells:
        cell.occupied = False
    for target in targets:
        target.cells_in_range = []


def get_new_positions(robots_dict, cells_dict, targets):
    """
    new_positions: new_positions[robot.name] = robot.pos
    """
    new_positions = {}
    for robot_name, robot in robots_dict.items():
        robot.prev_pos = robot.pos
        robot.pos = get_robot_pos_dsa_mst(robot_name, robot, targets, robots_dict)
        new_positions[robot.name] = robot.pos
    return new_positions


def get_robot_pos_dsa_mst(robot_name, robot, targets, robots_dict):
    """
    # TODO: temp_req_set
    # TODO: select_pos
    # TODO: if dsa_condition

    SELECT_POS ( select_pos(pos_set, targets, SR) ):
        input:
        pos_set = [(x1, y1),(x2, y2),..]
        targets = [(target, temp_req), (target, temp_req), ..]
        SR = int()
        output:
        pos = (x, y)
    """
    neighbours = get_neighbours(robot, robots_dict)
    temp_req_set = calculate_temp_req(targets, neighbours)
    pos_set = get_pos_set(robot)
    new_pos = select_pos(pos_set, temp_req_set, SR)
    if dsa_condition(robot, new_pos, robot.pos, temp_req_set):
        return new_pos
    return robot.pos


def dsa_condition(agent, new_pos, curr_pos, temp_req_set):
    """
    input:
    output:
    More specifically, in DSA, the replacement
    decision takes into account whether a replacement of assignment will improve the
    local state of the agent. If so, a change is made with probability defined by parameter
    p. Zhang et al. showed that the value of p has a major effect on the quality of solutions
    found by DSA [63].
    """
    curr_value = 0
    new_value = 0
    for (target, temp_req) in temp_req_set:
        if in_area(new_pos, target.get_pos(), agent.get_SR()):
            new_value += min(agent.get_cred(), temp_req)
        if in_area(curr_pos, target.get_pos(), agent.get_SR()):
            new_value += min(agent.get_cred(), temp_req)
    if new_value >= curr_value:
        return random.random() < 0.7
    return False


def get_neighbours(robot1, robots_dict):
    neighbour_robots = []
    for robot2_name, robot2 in robots_dict.items():
        if robot1.name != robot2_name:
            if distance(robot1.pos, robot2.pos) < 2 * (SR + MR):
                neighbour_robots.append(robot2)
    return neighbour_robots


def calculate_temp_req(targets, neighbours):
    """
    input:
    output:
    """
    temp_req_set = []
    for target in targets:
        curr_tuple = (target, target.get_req())
        for nei in neighbours:
            if in_area(nei.get_pos(), target.get_pos(), SR):
                curr_tuple = (target, max(0, curr_tuple[1] - nei.get_cred()))
        temp_req_set.append(curr_tuple)
    return temp_req_set


def get_pos_set(robot):
    """
    cells in MR: robot.neighbours
    """
    pos_set = []
    for cell in robot.neighbours:
        pos_set.append(cell.pos)
    return pos_set
