# in the extreme situation, we got a string with ascending sequence of the numbers, then we remove anymore digits the number
# is definitely smaller than the previous one. this is because the higher digit larger than corresponding higher digit then
# the number must be larger. So we try to remove from higher digit to ensure new num is as ascending as possible
# if more digit need to be removed we remove from the end since the end is larger than the head
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k > 0:
            stack.pop()
            k -= 1
        result = "".join(stack).lstrip("0")
        if len(result) == 0:
            return "0"
        return result
    
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        new = ""
        for i in range(n):
            while k > 0 and i > 0 and int(num[i]) < int(new[-1]):
                new = new[:-1]
                k -= 1
            new = new + num[i]

        while k > 0:
            new = new[:-1]
            k -= 1
        while new[0] == "0":
            new = new[1:]
        if len(new) == 0:
            return "0"
        return new
    
solution = Solution()
print(solution.removeKdigits(num = "1432219", k = 3))
print(solution.removeKdigits(num = "10200", k = 1))
