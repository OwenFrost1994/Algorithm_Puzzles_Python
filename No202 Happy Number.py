class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        slow = self.square(slow)
        fast = self.square(self.square(fast))
        while slow != fast:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
        
        return slow == 1

    def square(self, num):
        ans = 0
        
        while num > 0:
            remainder = num % 10
            ans += remainder * remainder
            num = num//10
        
        return ans
    
class Solution1:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        ch=False
        if n=='1':
            ch=True
        else:
            while n not in ('2', '3', '4', '5', '6', '8','9'):
                print(n,1)
                s=0
                for i in n:
                    s+=int(i)**2
                if s==1:
                    ch=True
                    break
                else:
                    n=str(s)
        return ch
    
solution = Solution()

n = 19
print(solution.isHappy(n))

n = 12
print(solution.isHappy(n))

n = 2
print(solution.isHappy(n))