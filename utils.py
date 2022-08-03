import pygame

def scale_image(image, factor):
    new_width = round(image.get_width() * factor)
    new_height = round(image.get_height() * factor)
    new_size = (new_width, new_height)
    return pygame.transform.scale(image, new_size)

class jim_the_jelly:
    def __init__(self, sf:int=1):
        self.scale = sf

    @property
    def right(self):
        return scale_image(pygame.image.load("imgs/right.png"), self.scale)

    @property
    def left(self):
        return scale_image(pygame.image.load("imgs/left.png"), self.scale)
