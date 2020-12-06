from CONSTANTS import *
from pure_functions import *


def random_walk(params, all_agents):
    robots, targets, cells, robots_dict, cells_dict = separate_all_agents(all_agents)
    clear_domains_and_neighbours_update_runds_update_cells(all_agents, robots, targets, cells)
    set_robots_domains_and_neighbours_for_robots_and_cells(robots, cells)

    new_random_positions = get_new_random_positions(robots_dict, cells_dict)

    return new_random_positions, calc_collisions(new_random_positions)


def set_robots_domains_and_neighbours_for_robots_and_cells(robots, cells):
    mark_occupied_cells_by_robots(robots, cells)
    for robot in robots:
        for cell in cells:
            dist = distance(robot.get_pos(), cell.get_pos())
            if dist <= DISTANCE_BETWEEN_CELLS:
                if dist == 0 or not cell.occupied:
                    robot.domain.append(cell.num)
                    robot.neighbours.append(cell)
                    cell.neighbours.append(robot)


def mark_occupied_cells_by_robots(robots, cells):
    for robot in robots:
        for cell in cells:
            dist = distance(robot.get_pos(), cell.get_pos())
            if dist == 0:
                cell.occupied = True
                break


def clear_domains_and_neighbours_update_runds_update_cells(all_agents, robots, targets, cells):
    for agent in all_agents:
        agent.neighbours = []
        if LOAD_PREVIOUS_WEIGHTS:
            agent.rund = load_weight_of(agent.name, file_name)['rund']
        else:
            agent.update_rund()
    for robot in robots:
        robot.domain = []
        # robot.prev_pos = robot.pos
    for cell in cells:
        cell.occupied = False
    for target in targets:
        target.cells_in_range = []


def get_new_random_positions(robots_dict, cells_dict):
    new_positions = {}
    for robot_name, robot in robots_dict.items():
        robot.prev_pos = robot.pos
        robot.pos = cells_dict[random.choice(robot.domain)].pos
        new_positions[robot.name] = robot.pos
    return new_positions
