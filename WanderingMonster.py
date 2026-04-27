import random

class WanderingMonster:
    def __init__(self, x, y, monster_type, color, hp):
        self.x = x                  # int
        self.y = y                  # int
        self.monster_type = monster_type  # string
        self.color = list(color)    # make sure JSON-safe
        self.hp = hp                # int

    @classmethod
    def random_spawn(cls, occupied, forbidden, grid_w, grid_h):
        while True:
            x = random.randint(0, grid_w - 1)
            y = random.randint(0, grid_h - 1)

            if (x, y) not in occupied and (x, y) not in forbidden:
                return cls(
                    x,
                    y,
                    monster_type="Swamp Goblin",
                    color=[0, 200, 0],
                    hp=10
                )

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["x"],
            data["y"],
            data["monster_type"],
            data["color"],
            data["hp"]
        )

    def to_dict(self):
        return {
            "x": self.x,
            "y": self.y,
            "monster_type": self.monster_type,
            "color": self.color,
            "hp": self.hp
        }

    def move(self, occupied, forbidden, grid_w, grid_h):
        directions = [
            (0, 1),   # down
            (0, -1),  # up
            (1, 0),   # right
            (-1, 0)   # left
        ]

        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if (
                0 <= new_x < grid_w and
                0 <= new_y < grid_h and
                (new_x, new_y) not in occupied and
                (new_x, new_y) not in forbidden
            ):
                self.x = new_x
                self.y = new_y
                return  # move once

        # if no valid moves → stays in place