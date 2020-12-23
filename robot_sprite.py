# Import the pygame module
from CONSTANTS import *
# from pure_functions import *


# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class RobotSprite(pygame.sprite.Sprite):
    def __init__(self,
                 cell_size=CELL_SIZE['BIG'],
                 number_of_robot=0,
                 surf_center=-1,
                 MR=round(3.5 * CELL_SIZE['BIG']),
                 SR=int(2.5 * CELL_SIZE['BIG']),
                 show_ranges=False,
                 speed=10,
                 cred=5,
                 ):
        super(RobotSprite, self).__init__()
        self.cell_size = cell_size
        self.num_of_agent = number_of_robot
        self.name = 'robot_%s' % number_of_robot
        self.MR = int(MR)
        self.SR = int(SR)
        self.cred = cred
        self.show_ranges = show_ranges
        self.curr = (3, -3)
        self.future_pos = None
        self.arrived = True
        self.step_x = 0
        self.step_y = 0
        self.speed = speed
        self.direction = np.random.randint(360)  # degrees
        self.curr_nei = []
        self.curr_robot_nei = []
        self.inbox = {}
        self.named_inbox = {}
        self.tuple_keys_inbox = {}
        self._lock = threading.RLock()
        self.cells = []
        self.targets = []
        self.target_nei_tuples = []
        self.robot_nei_tuples = []
        self.all_nei_tuples = []

        self.surf = pygame.Surface((2 * MR, 2 * MR), pygame.SRCALPHA)

        if show_ranges:
            pygame.draw.circle(self.surf, (0, 0, 255, 20), self.surf.get_rect().center, self.MR)
            pygame.draw.circle(self.surf, (255, 0, 0, 40), self.surf.get_rect().center, self.SR)

        self.car_surf = pygame.transform.scale(pygame.image.load("pics/hamster2.png"), (cell_size, int(0.73 * cell_size)))
        self.car_surf.set_colorkey((255, 255, 255), RLEACCEL)

        # Number of Robot
        font = pygame.font.SysFont("comicsansms", int(cell_size * 0.25))
        text = font.render("%s" % number_of_robot, True, (225, 0, 0))
        wt, ht = text.get_size()
        self.car_surf.blit(text, (cell_size - wt, 0))

        self.surf.blit(self.car_surf, self.car_surf.get_rect(center=self.surf.get_rect().center))

        if surf_center == -1:
            self.rect = self.surf.get_rect()
            print('[ERROR]: surf_center == -1 in Agent')
        else:
            self.surf_center = surf_center
            self.rect = self.surf.get_rect(
                center=surf_center
            )
            self.radius = MR

    # Move the sprite based on user keypresses
    def move(self):
        # logging.info("Thread %s : starting moving", threading.get_ident())

        self.arrived = self.rect.center == self.future_pos

        if not self.arrived:

            curr_x, curr_y = self.rect.center
            future_x, future_y = self.future_pos

        # if self.rect.center == self.future_pos:
        #     self.arrived = True
        # else:

            x = self.step_x if abs(curr_x - future_x) > abs(self.step_x) else (future_x - curr_x)
            y = self.step_y if abs(curr_y - future_y) > abs(self.step_y) else (future_y - curr_y)

            # self.rect.move_ip(x, y)
            self.rect.center = (curr_x + x, curr_y + y)

            # print(self.get_name(), ' in move function', ' ', self.rect.center, ' ', self.future_pos,
            #       ' steps:', self.step_x, self.step_y, ' x and y:', x, y)

    def preprocessing(self, **kwargs):
        # print('in preprocessing')
        return kwargs

    # different from other because the agent is moving -> NOT self.surf_center
    def get_pos(self):
        return self.rect.center

    def get_cell_size(self):
        return self.cell_size

    def set_pos(self, pos):
        self.rect.center = pos
        self.future_pos = pos

    def get_SR(self):
        return self.SR

    def get_MR(self):
        return self.MR

    def get_name(self):
        return self.name

    def get_cred(self):
        return self.cred

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction


    def get_num_of_agent(self):
        return self.num_of_agent





