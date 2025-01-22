# 类似一个random sampling and acceptance/rejection的模拟仿真，这有不同的实现方法，现在写的是跟我一开始想的不一样的方法
from math import cos, pi, sin
from random import random

class Solution:

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        theta = 2*pi*random()
        r = random()
        return [self.x + r*self.radius*cos(theta), self.y + r*self.radius*sin(theta)]
    
solution = Solution(1,0,0)
print(solution.randPoint())
print(solution.randPoint())
print(solution.randPoint())

solution = Solution(10,5,-7.5)
print(solution.randPoint())
print(solution.randPoint())
print(solution.randPoint())