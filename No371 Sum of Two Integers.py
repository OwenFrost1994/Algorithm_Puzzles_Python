class Solution: # no mast, no overflow consideration
  def getSum(self, a: int, b: int) -> int:
    if b == 0:
        return a

    sum = a ^ b  # Step 1: sum without carry
    carry = (a & b) << 1  # Step 2: calculate carry

    return self.getSum(sum, carry)
  
  def getSum(self, a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    kMax = 0x80000000
    # the result of each step is passed recursively to the getSum function 
    # until there is no carry (b == 0)
    # at that point, the function returns the final sum.
    while b:
      a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return a if a < kMax else ~(a ^ mask)