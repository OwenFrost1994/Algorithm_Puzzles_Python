class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s: str):
        if not s:
            return NestedInteger()
        if s[0] != "[":
            return NestedInteger(int(s))
        if len(s) <= 2:
            return NestedInteger()
        result = NestedInteger()
        i = 1
        depth = 0
        for j in range(1, len(s)):
            if depth == 0 and (s[j] == "," or j == len(s) - 1):
                result.add(self.deserialize(s[i:j]))
                i = j + 1
            elif s[j] == "[":
                depth += 1
            elif s[j] == "]":
                depth -= 1
        return result