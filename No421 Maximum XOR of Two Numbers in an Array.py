from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        result = 0
        digit = 0
        maxn = max(nums)
        while maxn > 0:
            digit += 1
            maxn = maxn//2
        for i in range(digit)[::-1]:
            result <<= 1
            prefixes = {num >> i for num in nums}
            # compare = []
            # for p in prefixes:
            #     print(result^1)
            #     print(result^1 ^p)
            #     compare.append(result^1 ^p in prefixes)
            result += any(result^1 ^ p in prefixes for p in prefixes)
            # result += any(compare)
        return result

# tire method
class TrieNode:
    def __init__(self):
        self.children = dict()                        # children nodes
        self.val = 0       
class Trie:
    def __init__(self, n):
        self.root = TrieNode()                        # root node
        self.n = n                                    # max length of all numbers
    
    def add_num(self, num):
        node = self.root 
        for shift in range(self.n, -1, -1):           # only shift self.n bits 
            val = 1 if num & (1 << shift) else 0      # verify bit from left to right 
            if val not in node.children:
                node.children[val] = TrieNode()
            node = node.children[val]
        node.val = num

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_len = len(bin(max(nums))) - 2             # get max length of all numbers' binary
        trie = Trie(max_len)
        for num in nums: trie.add_num(num)            # build trie
            
        ans = 0
        for num in nums:                              # for each num, find the number which can create max value with num using XOR
            node = trie.root 
            for shift in range(max_len, -1, -1):
                val = 1 if num & (1 << shift) else 0  # verify bit from left to right
                node = node.children[1-val] if 1-val in node.children else node.children[val] # try opposite bit first, otherwise use same bit
            ans = max(ans, num ^ node.val)            # maintain maximum
        return ans
    
solution = Solution()
print(solution.findMaximumXOR([3,10,5,25,2,8]))
print(solution.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))