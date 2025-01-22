class Solution:
    def canCompleteCircuit(self, gas, cost):
        for i in range(len(gas)):
            move = i
            if gas[move] == 0 or gas[move] < cost[i]:
                continue
            loopcount = 0
            gastank = 0
            while loopcount < len(gas):
                gastank = gastank + gas[move] - cost[move]
                if gastank >= 0:
                    move += 1
                    move = move % len(gas)
                    loopcount += 1
                else:
                    i + 1
                    break
            if loopcount == len(gas):
                return i
        return -1

class Solution1:
    def canCompleteCircuit(self, gas, cost) -> int:
        n, total_surplus, surplus, start = len(gas), 0, 0, 0
        
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            surplus += gas[i] - cost[i]
            if surplus < 0:
                surplus = 0
                start = i + 1
        return -1 if (total_surplus < 0) else start

solution = Solution()

gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(solution.canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(solution.canCompleteCircuit(gas, cost))

gas = [3,3,4]
cost = [3,4,4]
print(solution.canCompleteCircuit(gas, cost))

gas = [4,5,2,6,5,3]
cost = [3,2,7,3,2,9]
print(solution.canCompleteCircuit(gas, cost))