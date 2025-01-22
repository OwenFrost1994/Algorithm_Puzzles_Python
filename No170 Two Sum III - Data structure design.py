from collections import Counter
class TwoSum:
    def __init__(self):
        self.cnt = Counter()

    def add(self, number: int) -> None:
        self.cnt[number] += 1

    def find(self, value: int) -> bool:
        for x, v in self.cnt.items():
            y = value - x
            if y in self.cnt:
                # v > 1, for case: add=3, add=3, target=6
                if x != y or v > 1:
                    return True
        return False