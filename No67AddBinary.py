class Solution:
  def addBinary(self, a, b):
    result = ""
    len1 = len(a)
    len2 = len(b)
    length = max(len1, len2)
    isadd = 0
    while(length > 0):
        num1 = 0
        num2 = 0
        if len1 > 0:
            num1 = ord(a[len1-1]) - ord('0')
        if len2 > 0:
            num2 = ord(b[len2-1]) - ord('0')
        if num1 + num2 + isadd == 3:
           result = "1" + result
           isadd = 1
        elif num1 + num2 + isadd == 2:
           result = "0" + result
           isadd = 1
        elif num1 + num2 + isadd == 1:
           result = "1" + result
           isadd = 0
        else:
           result = "0" + result
           isadd = 0
        
        length -= 1
        len1 -= 1
        len2 -= 1
    if isadd == 1:
       result = "1" + result
    return result

a = "11"
b = "1"
solution = Solution()
print(solution.addBinary(a, b))

a = "1010"
b = "1011"
solution = Solution()
print(solution.addBinary(a, b))

# class Solution:
#   def addBinary(self, a, b):
#     s = []
#     carry = 0
#     i = len(a) - 1
#     j = len(b) - 1

#     while i >= 0 or j >= 0 or carry:
#       if i >= 0:
#         carry += int(a[i])
#         i -= 1
#       if j >= 0:
#         carry += int(b[j])
#         j -= 1
#       s.append(str(carry % 2))
#       carry //= 2

#     return ''.join(reversed(s))