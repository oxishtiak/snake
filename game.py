import os
import time
import msvcrt
import random

from snek import Snake
from food import StaticFood, MovingFood, BigFood

# Game class
class Game:
    def __init__(self, width=40, height=20):
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