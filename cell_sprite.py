from CONSTANTS import *


class CellSprite(pygame.sprite.Sprite):
    def __init__(self, cell_size=CELL_SIZE, order=-1, surf_center=-1):
        super(CellSprite, self).__init__()
        self.cell_size = cell_size
        self.surf = pygame.Surface((cell_size, cell_size))
        self.surf.fill((255, 255, 255))
        if surf_center == -1:
            print('[ERROR]: surf_center == -1 in Cell')
        else:
            self.surf_center = surf_center
            self.rect = self.surf.get_rect(
                center=surf_center
            )
        self.prop = None
        self.num_of_agent = order
        self.name = 'cell_%s' % order

    def update(self):
        pass

    def add_property(self, prop):
        self.prop = prop

    def get_prop(self):
        return self.prop

    def get_pos(self):
        return self.rect.center

    def get_num_of_agent(self):
        return self.num_of_agent
