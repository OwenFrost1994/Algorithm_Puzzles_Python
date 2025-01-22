# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """

# 这个系统跟物理交互，如果一个方向不对，需要turnright，然后再看下一个方向是不是能走
# 他需要一个循环搜索不同方向的办法(d + i) % 4一开始还走原来的方向, 为了防止走完一个方向发现后面都清理了被trap住,需要back()函数
class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(x, y, d):
            visited.add((x, y))
            robot.clean()
            for i in range(4):
                nd = (d + i) % 4
                nx = x + direct[nd][0]
                ny = y + direct[nd][1]
                if (nx, ny) not in visited and robot.move():
                    dfs(nx, ny, nd)
                    back()
                robot.turnRight()

        visited = set()
        direct = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 每次转90度
        dfs(0, 0, 0)