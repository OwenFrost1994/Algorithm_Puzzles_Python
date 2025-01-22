from collections import defaultdict


class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = {}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.counter.keys():
            self.counter[timestamp] = 1
        else:
            self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        return sum([v for k, v in self.counter.items() if k + 300 >= timestamp + 1])

hitCounter = HitCounter()
# print(hitCounter.hit(1)) # hit at timestamp 1.
# print(hitCounter.hit(2)) # hit at timestamp 2.
# print(hitCounter.hit(3)) # hit at timestamp 3.
# print(hitCounter.getHits(4)) # get hits at timestamp 4, return 3.
# print(hitCounter.hit(300)) # hit at timestamp 300.
# print(hitCounter.getHits(300)) # get hits at timestamp 300, return 4.
# print(hitCounter.getHits(301)) # get hits at timestamp 301, return 4.

print(hitCounter.hit(1)) # hit at timestamp 1.
print(hitCounter.hit(2)) # hit at timestamp 2.
print(hitCounter.hit(3)) # hit at timestamp 3.
print(hitCounter.getHits(4)) # get hits at timestamp 4, return 3.
print(hitCounter.hit(300)) # hit at timestamp 300.
print(hitCounter.getHits(300)) # get hits at timestamp 300, return 4.
print(hitCounter.getHits(301)) # get hits at timestamp 301, return 3.