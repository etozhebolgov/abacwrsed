import pygame
import yaml

from terrain import (
    Wall_H,
    Wall_V,
    Wall_H_JD,
    Wall_VE_JU,
    Barrier,
    SadBarrier,
    HappyBarrier,
)

def get_building_argumets(room):
    """
    Function takes .yml file for specific room with:
    - position : (x, y) - left upper corner
    - size : (a, b) - lengths of sides of a rectangle
    - name : str

    Variable room contains path to .yml file with that room configuration.
    """

    with open(room, 'r') as f:
        config = yaml.safe_load(f)
    print(config)

    position = (int(config['position_x']), int(config['position_y']))
    length = int(config['length'])
    height = int(config['height'])

    return position, length, height

def building_configuration(boxes, camera_group, room):
    """
    Builds a room from position, length and height
    """
    position, length, height = get_building_argumets(room)
    x, y = position

    for dx in range(0, length, 70):
            boxes.add(Wall_H(x + dx, y, camera_group))
            boxes.add(Wall_H(x + dx, y + height, camera_group))
    for dy in range(0, height + 70, 70):
            boxes.add(Wall_V(x, y + dy, camera_group))
            boxes.add(Wall_V(x + length, y + dy, camera_group))

    return boxes


def create_custom_walls(camera_group):
    """
    Creates a custom set of walls for the game
    """
    boxes = pygame.sprite.Group()
    boxes = building_configuration(boxes, camera_group, 'Rooms\hub.yml')


    return boxes