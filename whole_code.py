import random
import os
import time
import msvcrt  # For real-time key handling on Windows

# Base class: Food
class Food:
    def __init__(self, width, height):
        self.width = width
        self.height = height
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
    
    def move(self):
        self.position = (random.randint(0, self.width - 1), random.randint(0, self.height - 1))

class BigFood(Food):
    def __init__(self, board_width, board_height):
        super().__init__(board_width, board_height)
    
    def get_points(self): #overriding
        return 5  # Big food gives more points

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

# Game class
class Game:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.food_items = [
            StaticFood(self.width, self.height),
            MovingFood(self.width, self.height),
            BigFood(self.width, self.height)
        ]
        self.score = 0

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]

        for segment in self.snake.body:
            x, y = segment
            board[y][x] = 'o'

        for food in self.food_items:
            food_x, food_y = food.position
            board[food_y][food_x] = 'x'

        for row in board:
            print('|' + ''.join(row) + '|')
        print(f"Score: {self.score}")

    def update(self):
        self.snake.move()

        for food in self.food_items:
            if isinstance(food, MovingFood):
                food.move()

            if self.snake.body[0] == food.position:
                self.snake.grow()
                self.food_items.remove(food)
                self.food_items.append(random.choice([StaticFood(self.width, self.height), MovingFood(self.width, self.height), BigFood(self.width, self.height)]))
                self.score += food.get_points()

        head_x, head_y = self.snake.body[0]
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return False

        return True

    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            direction_map = {
                'w': 'UP',
                's': 'DOWN',
                'a': 'LEFT',
                'd': 'RIGHT'
            }
            if key in direction_map:
                self.snake.change_direction(direction_map[key])

    def run(self):
        while True:
            self.render()
            self.handle_input()
            if not self.update():
                print("Game Over!")
                break
            time.sleep(0.2)

# Start the game
if __name__ == "__main__":
    game = Game()
    game.run()
