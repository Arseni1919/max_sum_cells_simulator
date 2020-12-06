from CONSTANTS import *
from cell_sprite import *
from robot_sprite import *
from target_sprite import *
from title_sprite import *
from cell import *
from robot import *
from target import *
from variable_node import *
from function_node import *


def init_pygame():
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT + 202, SCREEN_HEIGHT), pygame.SRCALPHA)
    finish_sound = pygame.mixer.Sound("sounds/Bell_2.ogg")
    return clock, screen, finish_sound


def go_back_to_initial_positions(all_sprites, all_agents, screen):
    for sprite in all_sprites:
        for agent in all_agents:
            if sprite.name == agent.name:
                sprite.set_pos(agent.initial_pos)
                agent.pos = agent.initial_pos
                agent.prev_pos = agent.initial_pos
    first_screen_blit(screen, all_sprites)


def first_screen_blit(screen, all_sprites):
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Update the display
    pygame.display.flip()
    time.sleep(1)

def close_pygame(finish_sound):
    finish_sound.play()
    time.sleep(2)
    # All done! Stop and quit the mixer.
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # time.sleep(2)
    # Done! Time to quit.
    pygame.quit()


def pickle_results_if():
    pass


def plot_results_if():
    pass


def print_main(description, order, pred=''):
    logging.info("%s --- %s: %s --- " % (pred, description, order))
    # print(f' --- {description}: {order} --- ')

def init_problem(problem):
    all_sprites = create_all_sprites()
    all_agents = create_all_agents(all_sprites)
    reset_all(all_sprites, all_agents)
    return all_sprites, all_agents


def reset_all(all_sprites, all_agents):
    if LOAD_PREVIOUS_POSITIONS:
        for sprite in all_sprites:
            sprite.pos = load_weight_of(sprite.name, file_name)['pos']
        for agent in all_agents:
            # agent.rund = load_weight_of(agent.name, file_name)['rund']
            agent.pos = load_weight_of(agent.name, file_name)['pos']
            agent.prev_pos = load_weight_of(agent.name, file_name)['pos']
            agent.initial_pos = load_weight_of(agent.name, file_name)['pos']

# Create Field
def create_field(all_sprites, cells):
    num = 1
    for i in range(int(SCREEN_HEIGHT / (cell_size + PADDING))):
        for j in range(int(SCREEN_HEIGHT / (cell_size + PADDING))):
            surf_center = (
                PADDING + i * (cell_size + PADDING) + (cell_size / 2),
                PADDING + j * (cell_size + PADDING) + (cell_size / 2)
            )
            new_cell = CellSprite(cell_size, order=num, surf_center=surf_center)
            num += 1
            cells.add(new_cell)
            all_sprites.add(new_cell)


# Create targets
def create_targets(cell_size, all_sprites, targets, cells,
                   ratio=0.3,
                   req=-1,
                   use_rate=True,
                   num_of_targets=-1):
    order = 1
    if use_rate:
        for cell in cells.sprites():
            if random.random() < ratio:
                new_target = TargetSprite(
                    cell_size,
                    order=order,
                    req=req,
                    surf_center=cell.get_pos()
                )
                cell.prop = new_target
                targets.add(new_target)
                all_sprites.add(new_target)
                order += 1
    else:
        if num_of_targets == -1:
            print('[ERROR]: bad')
            raise RuntimeError('BADDDD')
        while True:
            cell = random.choice(cells.sprites())
            if not cell.prop:
                new_target = TargetSprite(
                    cell_size,
                    order=order,
                    req=req,
                    surf_center=cell.get_pos()
                )
                cell.prop = new_target
                targets.add(new_target)
                all_sprites.add(new_target)
                order += 1
                if num_of_targets == len(targets.sprites()):
                    break


def create_robots(cell_size, all_sprites, agents, cells,
                  num_of_agents=4,
                  ratio=0.05,
                  MR=round(3.5 * CELL_SIZE['BIG']),
                  SR=int(2.5 * CELL_SIZE['BIG']),
                  cred=5,
                  show_ranges=False,
                  speed=10):
    for agent in range(1, num_of_agents + 1):
        assigned = False
        while not assigned:
            indexes = [i for i in range(len(cells.sprites()))]
            random.shuffle(indexes)
            for index in indexes:
                cell = cells.sprites()[index]
                if random.random() < ratio and cell.prop is None:
                    new_agent = RobotSprite(cell_size=cell_size,
                                            number_of_robot=agent,
                                            surf_center=cell.get_pos(),
                                            MR=MR,
                                            SR=SR,
                                            cred=cred,
                                            show_ranges=show_ranges,
                                            speed=speed)
                    cell.prop = new_agent
                    agents.add(new_agent)
                    all_sprites.add(new_agent)
                    assigned = True
                    break


def create_dictionary(agents, targets):
    for agent in agents.sprites():
        OBJECTS[agent.get_name()] = agent
    for target in targets.sprites():
        OBJECTS[target.get_name()] = target


def create_all_sprites():
    # Create groups to hold all kinds of sprites
    # - all_sprites is used for rendering
    agents = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    # titles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Create Field
    create_field(all_sprites, cells)
    print('height/weight: ', math.sqrt(len(cells.sprites())))

    # Create targets on field
    create_targets(cell_size, all_sprites, targets, cells, target_rate, REQ, use_rate, num_of_targets)

    # Create agents on field
    create_robots(cell_size, all_sprites, agents, cells,
                  num_of_agents=num_of_agents,
                  MR=MR,
                  SR=SR,
                  cred=CRED,
                  show_ranges=show_ranges,
                  speed=speed)
    # add_cell_and_target_tuples(agents, cells, targets)
    create_dictionary(agents, targets)
    return all_sprites


def create_all_agents(all_sprites):
    all_agents = []
    for sprite in all_sprites:
        if 'robot' in sprite.name:
            all_agents.append(VariableNode(name=sprite.name, num=sprite.num_of_agent, domain=[], pos=sprite.get_pos()))
        elif 'target' in sprite.name:
            all_agents.append(FunctionNode(name=sprite.name, num=sprite.num_of_agent, func=None, pos=sprite.get_pos()))
        elif 'cell' in sprite.name:
            all_agents.append(FunctionNode(name=sprite.name, num=sprite.num_of_agent,
                                           func=func_cell, pos=sprite.get_pos()))
        else:
            raise RuntimeError('[ERROR]: unknown sprite')
    return all_agents


