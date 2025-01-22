from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        result = []
        for i in range(n):
            result.append(num)
            if num * 10 <= n:
                num *= 10 
            else:
                while num % 10 == 9 or num >= n:
                    num = num // 10
                num += 1
        return result

solution = Solution()
print(solution.lexicalOrder(8)) # [1 2 3 4 5 6 7 8]
print(solution.lexicalOrder(13)) # [1 10 11 12 13 14 15 16 17 18 19 2 3 4 5 6 7 8]
print(solution.lexicalOrder(19)) # [1 10 100 101 102 103 --- 109 11 110 111 112 113 ]
print(solution.lexicalOrder(113)) # [1 10 100 101 102 103 --- 109 11 110 111 112 113 12 13 14 15 16 17 18 19 2 20 21 22 23 24 25---]
print(solution.lexicalOrder(133))
