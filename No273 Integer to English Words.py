class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion", "Septillion", "Octillion", "Nonillion", "Decillion"]
        words = []
        i = 0
        while num > 0:
            triple = num % 1000
            num = num // 1000
            if triple == 0:
                i += 1
                continue
            temp = []
            if triple // 100 > 0:
                temp.append(ones[triple // 100])
                temp.append("Hundred")
            if triple % 100 >= 10 and triple % 100 <= 19:
                temp.append(teens[triple % 10])
            else:
                if triple % 100 >= 20:
                    temp.append(tens[triple % 100 // 10])
                if triple % 10 > 0:
                    temp.append(ones[triple % 10])
            if i > 0:
                temp.append(suffixes[i])
            i += 1
            words = temp + words
        return " ".join(words)
    
solution = Solution()
num = 123
print(solution.numberToWords(num))
num = 12345
print(solution.numberToWords(num))
num = 1234567
print(solution.numberToWords(num))