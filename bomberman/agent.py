# Daniel Coelho de Oliveira - 96800
# Pedro Candoso - 86140
# Miguel Matos - 89124

from utils import *


class Agent:

    def __init__(self, mapa, gstate=None):
        self.gstate = gstate
        self.mapa = mapa
        self.memory = []
        self.detonate = ""
        self.previousenemies = None
        self.radius = 2

    def get_enemy_goal(self, enemies):
        # enemies = (name, id, pos)
        if enemies[0] == 'Balloom':
            return (1, 1), "B"

        aux = self.tiles_around(tuple(enemies[2]), 2)
        togo = self.closest_tile(self.gstate['bomberman'], aux)[1]
        return tuple(togo), "B"

    def get_goal(self):
        # Agent decides it's goal
        player = self.gstate['bomberman']
        if self.previousenemies is None:
            self.previousenemies = self.gstate['enemies']
            return tuple(player), ""

        if self.gstate['powerups']:
            if self.gstate['powerups'][0][1] == 'Detonator':
                self.detonate = "A"
            aux = self.tiles_around(self.gstate['powerups'][0][0])
            a, b = self.closest_power(player, aux, self.gstate['powerups'][0][0])
            return a, b
        if self.gstate['bombs']:
            # check if bomberman is in safe location
            bombpos = self.gstate['bombs'][0][0]
            bombradius = self.gstate['bombs'][0][2]
            # learn the bomb radius
            self.radius = bombradius - 1
            explode_tiles = self.tiles_around(bombpos, 3)
            explode_tiles.append(bombpos)
            aux = []
            corner = [bombpos[0] - bombradius, bombpos[1] - bombradius]
            for x in range(bombradius * 2):
                for y in range(bombradius * 2):
                    if not self.mapa.is_blocked([corner[0] + x, corner[1] + y]):
                        aux.append([corner[0] + x, corner[1] + y])
            good_tiles = [t for t in aux if t not in explode_tiles]
            togo = self.closest_tile(player, good_tiles)[1]
            return tuple(togo), self.detonate

        if self.gstate['walls']:
            closest = self.closest_wall(player, self.gstate['walls'])[1]
            aux = self.tiles_around(closest, self.radius)
            togo = self.closest_tile(player, aux)[1]
            return tuple(togo), "B"
        if self.gstate['enemies']:
            # print(self.closest_enemy(self.gstate['enemies']))
            return self.get_enemy_goal(self.closest_enemy(self.gstate['enemies']))
        if self.gstate['exit']:
            aux = self.tiles_around(self.gstate['exit'])
            a, b = self.closest_power(player, aux, self.gstate['exit'])
            return a, b

    def closest_wall(self, pos: tuple, walls):
        if not walls:
            return []
        return min([(distance(pos, w), w) for w in walls])

    def tiles_around(self, pos, radius=1):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        validtiles = []
        for d in dirs:
            temp = []
            for r in range(1, radius + 1):
                newpos = [pos[0] + d[0] * r, pos[1] + d[1] * r]
                if not self.mapa.is_blocked(newpos):
                    temp.append(newpos)
                else:
                    break
            [validtiles.append(e) for e in temp]
        return validtiles

    def calc_balloom_path(self, pos, direction):
        if direction == [0, 0]:
            return [pos]
        x, y = direction[0], direction[1]
        path = []
        nx, ny = pos[0] + x, pos[1] + y
        while not self.mapa.is_blocked([nx, ny]):
            nx, ny = nx + x, ny + y
            path += [[nx, ny]]
        return path

    def closest_tile(self, pos, tiles):
        if not tiles:
            return [0, pos]
        return min([(distance(pos, w), w) for w in tiles])

    def closest_enemy(self, enemies):
        closest = enemies[0]['id']
        name = enemies[0]['name']
        tile = enemies[0]['pos']
        for e in enemies:
            if e['pos'] < tile:
                closest = e['id']
                tile = e['pos']
        return name, closest, tile

    def closest_power(self, pos, power_around, power):
        b = min([(distance(pos, w), w) for w in power_around])[1]
        coord = power[0] - b[0], power[1] - b[1]
        if coord == (1, 0):
            return tuple(b), "d"
        elif coord == (-1, 0):
            return tuple(b), "a"
        elif coord == (0, 1):
            return tuple(b), "s"
        elif coord == (0, -1):
            return tuple(b), "w"

    def get_safety(self, pos, bomb):
        pass

    def update_state(self, gstate):
        self.gstate = gstate
