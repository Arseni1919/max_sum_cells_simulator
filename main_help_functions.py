from CONSTANTS import *
from cell_sprite import *
from robot_sprite import *
from target_sprite import *
from title_sprite import *


def init_pygame():
    clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_HEIGHT + 202, SCREEN_HEIGHT), pygame.SRCALPHA)
    finish_sound = pygame.mixer.Sound("sounds/Bell_2.ogg")
    return clock, screen, finish_sound


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


def init_problem(problem):
    logging.info("---------- ---------- Problem: %s ---------- ----------" % (problem + 1))
    # Create groups to hold all kinds of sprites
    # - all_sprites is used for rendering
    agents = pygame.sprite.Group()
    targets = pygame.sprite.Group()
    cells = pygame.sprite.Group()
    titles = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # Create Field
    create_field(all_sprites, cells)
    print('height/weight: ', math.sqrt(len(cells.sprites())))

    # Create targets on field
    create_targets(cell_size, all_sprites, targets, cells, target_rate, target_range, use_rate, num_of_targets)

    # Create agents on field
    create_agents(cell_size, all_sprites, agents, cells,
                  num_of_agents=num_of_agents,
                  MR=MR,
                  SR=SR,
                  cred=cred,
                  show_ranges=show_ranges,
                  speed=speed)
    # add_cell_and_target_tuples(agents, cells, targets)
    create_dictionary(agents, targets)
    return all_sprites


# Create Field
def create_field(all_sprites, cells):
    num = 1
    for i in range(int(SCREEN_HEIGHT / (cell_size + 2))):
        for j in range(int(SCREEN_HEIGHT / (cell_size + 2))):
            surf_center = (
                2 + i * (cell_size + 2) + (cell_size / 2),
                2 + j * (cell_size + 2) + (cell_size / 2)
            )
            new_cell = CellSprite(cell_size, order=num, surf_center=surf_center)
            num += 1
            cells.add(new_cell)
            all_sprites.add(new_cell)


# Create targets
def create_targets(cell_size, all_sprites, targets, cells,
                   ratio=0.3,
                   target_range=(1, 4),
                   use_rate=True,
                   num_of_targets=-1):
    order = 1
    if use_rate:
        for cell in cells.sprites():
            if random.random() < ratio:
                new_target = TargetSprite(
                    cell_size,
                    order=order,
                    req=random.randint(target_range[0], target_range[1]),
                    surf_center=cell.surf_center
                )
                cell.prop = new_target
                targets.add(new_target)
                all_sprites.add(new_target)
                order += 1
    else:
        if num_of_targets == -1:
            print('[ERROR]: bad')
        while True:
            cell = random.choice(cells.sprites())
            if not cell.prop:
                new_target = TargetSprite(
                    cell_size,
                    order=order,
                    req=random.randint(target_range[0], target_range[1]),
                    surf_center=cell.surf_center
                )
                cell.prop = new_target
                targets.add(new_target)
                all_sprites.add(new_target)
                order += 1
                if num_of_targets == len(targets.sprites()):
                    break


def create_agents(cell_size, all_sprites, agents, cells,
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
                                            surf_center=cell.surf_center,
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
