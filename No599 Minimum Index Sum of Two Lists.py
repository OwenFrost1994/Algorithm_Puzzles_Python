from math import inf
from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []
        m = inf
        mp = {v: i for i, v in enumerate(list1)}
        for i, w in enumerate(list2):
            if w in mp.keys():
                if i + mp[w] == m:
                    result.append(w)
                elif i + mp[w] < m:
                    m = i + mp[w]
                    result = [w]
        return result
    
solution = Solution()
print(solution.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
print(solution.findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]))
print(solution.findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))