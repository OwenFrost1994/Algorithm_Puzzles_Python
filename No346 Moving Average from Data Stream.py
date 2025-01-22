class MovingAverage:
    def __init__(self, size: int):
        self.nums = [0] * size
        self.sum = 0
        self.index = 0

    def next(self, val: int) -> float:
        idx = self.index % len(self.nums)
        self.sum += val - self.nums[idx]
        self.nums[idx] = val
        self.index += 1
        return self.sum / min(self.index, len(self.nums))
