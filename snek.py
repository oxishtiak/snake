# Snake class
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = 'RIGHT'

    def move(self):
        head_x, head_y = self.body[0]
        direction_map = {
            'UP': (head_x, head_y - 1),
            'DOWN': (head_x, head_y + 1),
            'LEFT': (head_x - 1, head_y),
            'RIGHT': (head_x + 1, head_y)
        }
        new_head = direction_map[self.direction]
        self.body = [new_head] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, new_direction):
        self.direction = new_direction