class Logger:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.limiter = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.limiter.keys():
            self.limiter[message] = timestamp + 10
            return True
        else:
            if self.limiter[message] <= timestamp:
                self.limiter[message] += 10
                return True
            else:
                return False
# 下面这个没有效率问题
class Logger:
    def __init__(self):
        self.limiter = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        t = self.limiter.get(message, 0)
        if timestamp < t:
            return False
        self.limiter[message] = timestamp + 10
        return True
logger = Logger()
print(logger.shouldPrintMessage(1, "foo")) # return true, next allowed timestamp for "foo" is 1 + 10 = 11
print(logger.shouldPrintMessage(2, "bar")) # return true, next allowed timestamp for "bar" is 2 + 10 = 12
print(logger.shouldPrintMessage(3, "foo")) # 3 < 11, return false
print(logger.shouldPrintMessage(8, "bar")) # 8 < 12, return false
print(logger.shouldPrintMessage(10, "foo")) # 10 < 11, return false
print(logger.shouldPrintMessage(11, "foo")) # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
 