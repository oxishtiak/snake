import random

# Base class: Food
class Food:
    def __init__(self, width, height):
        self.board_width = width
        self.board_height = height
        self.position = (random.randint(0, width - 1), random.randint(0, height - 1))

    def get_points(self):
        return 1  # Default point value

class StaticFood(Food):
    def __init__(self, board_width, board_height):
        super().__init__(board_width, board_height)
    # No extra behavior

class MovingFood(Food):
    def __init__(self, board_width, board_height):
        super().__init__(board_width, board_height)
        self.move_counter = 0  # Control how often it moves
    
    # def move(self):
    #     self.position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))
    
    def move(self):
        # Moves after a few updates
        if self.move_counter % 5 == 0:  # Move every 5th update
            x, y = self.position
            x = min(max(0, x + random.choice([-1, 1])), self.board_width - 1)
            y = min(max(0, y + random.choice([-1, 1])), self.board_height - 1)
            self.position = (x, y)
        self.move_counter += 1

class BigFood(Food):
    def __init__(self, board_width, board_height):
        super().__init__(board_width, board_height)
    
    def get_points(self): #overriding
        return 5  # Big food gives more points