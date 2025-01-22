class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.provided = [False] * maxNumbers

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        for i in range(len(self.provided)):
            if not self.provided[i]:
                self.provided[i] = True
                return i
        return -1

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        return not self.provided[number]

    def release(self, number: int) -> None:
        self.provided[number] = False

phoneDirectory = PhoneDirectory(3)
print(phoneDirectory.get()) # It can return any available phone number. Here we assume it returns 0.
print(phoneDirectory.get()) # Assume it returns 1.
print(phoneDirectory.check(2)) # The number 2 is available, so return true.
print(phoneDirectory.get()) # It returns 2, the only number that is left.
print(phoneDirectory.check(2)) # The number 2 is no longer available, so return false.
print(phoneDirectory.release(2)) # Release number 2 back to the pool.
print(phoneDirectory.check(2)) # Number 2 is available again, return true.
