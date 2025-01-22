# 1-7是均匀分布的，因此1-49也是均匀分布的，1-40也是，这样取%10，最后一位也是
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        # while True:
        #     # Generate a number in the range [1, 49] using rand7() twice
        #     num = (rand7() - 1) * 7 + rand7()
            
        #     # Reject numbers outside the range [1, 40]
        #     if num <= 40:
        #         break
        
        # # Return a number in the range [1, 10] using modulus
        # return num % 10 + 1
