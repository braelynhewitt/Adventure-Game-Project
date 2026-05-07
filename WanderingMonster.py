import random

class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        self.x = x
        self.y = y
        self.monster_type = monster_type
        self.color = color
        self.hp = hp

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": self.color,
            "hp": self.hp
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["x"],
            data["y"],
            data["monster_type"],
            data["color"],
            data["hp"]
        )

    @staticmethod
    def random_spawn(occupied, forbidden, grid_w, grid_h):
        while True:
            x = random.randint(0, grid_w - 1)
            y = random.randint(0, grid_h - 1)

            if (x, y) not in occupied and (x, y) not in forbidden:
                return x, y

    def move(self, occupied, forbidden, grid_w, grid_h):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = self.x + dx, self.y + dy

            if 0 <= nx < grid_w and 0 <= ny < grid_h:
                if (nx, ny) not in occupied and (nx, ny) not in forbidden:
                    self.x, self.y = nx, ny
                    return