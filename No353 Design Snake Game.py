from collections import deque
class SnakeGame(object):
    def __init__(self, width, height, food):
        self.snake = deque([[0, 0]])
        self.width = width
        self.height = height
        self.food = deque(food)
        self.score = 0
        self.direction = {"L": [0, -1], "R": [0, 1], "U": [-1, 0], "D": [1, 0]}
        
    def move(self, direction):
        if direction not in self.direction:
            return -1
        di, dj = self.direction[direction]
        ni, nj = self.snake[0][0] + di, self.snake[0][1] + dj
        if ni < 0 or ni >= self.height or nj < 0 or nj >= self.width:
            return -1
        if [ni, nj] in self.snake and [ni, nj] != self.snake[-1]:
            return -1
        if len(self.food) != 0 and [ni, nj] == self.food[0]:
            self.snake.appendleft([ni, nj])
            self.food.popleft()
            self.score += 1
        else:
            self.snake.appendleft([ni, nj])
            self.snake.pop()

        return self.score


# snakeGame = SnakeGame(3, 2, [[1, 2], [0, 1]])
# print(snakeGame.move("R")) # 0
# print(snakeGame.move("D")) # 0
# print(snakeGame.move("R")) # 1
# print(snakeGame.move("U")) # 1
# print(snakeGame.move("L")) # 2
# print(snakeGame.move("U")) # -1
# snakeGame = SnakeGame(2, 2, [[1, 0]])
# print(snakeGame.move("R"))
# print(snakeGame.move("D"))
# print(snakeGame.move("L"))
# print(snakeGame.move("U"))
# print(snakeGame.move("R"))
snakeGame = SnakeGame(3,3,[[2,0],[0,0],[0,2],[2,2]])
print(snakeGame.move("D")) # 0
print(snakeGame.move("D")) # 1
print(snakeGame.move("R")) # 1
print(snakeGame.move("U")) # 1
print(snakeGame.move("U")) # 1
print(snakeGame.move("L")) # 2
print(snakeGame.move("D")) # 2
print(snakeGame.move("R")) # 2
print(snakeGame.move("R")) # 2
print(snakeGame.move("U")) # 3
print(snakeGame.move("L")) # 3
print(snakeGame.move("D")) # 3

# snakeGame = SnakeGame(3,3,[[2,0],[0,0],[0,2],[0,1],[2,2],[0,1]])
# print(snakeGame.move("D")) # 0
# print(snakeGame.move("D")) # 1
# print(snakeGame.move("R")) # 1
# print(snakeGame.move("U")) # 1
# print(snakeGame.move("U")) # 1
# print(snakeGame.move("L")) # 2
# print(snakeGame.move("D")) # 2
# print(snakeGame.move("R")) # 2
# print(snakeGame.move("R")) # 2
# print(snakeGame.move("U")) # 3
# print(snakeGame.move("L")) # 4
# print(snakeGame.move("L")) # 4
# print(snakeGame.move("D")) # 4
# print(snakeGame.move("R")) # 4
# print(snakeGame.move("U")) # 4
