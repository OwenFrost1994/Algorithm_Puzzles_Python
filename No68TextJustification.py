# class Solution:
#     def fullJustify(self, words, maxWidth):
#         result = []
#         curr = ""
#         for word in words:
#             if len(curr) == 0:
#                 curr = word
#                 continue
#             if len(curr) + len(word) + 1 <= maxWidth:
#                 curr = curr + " " + word
#             else:
#                 result.append(curr)
#                 curr = word
#         return result

class Solution:
    def fullJustify(self, words, maxWidth):
        result, cur, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                cur, num_of_letters = [], 0

            cur += [word]
            num_of_letters += len(word)
        return result + [' '.join(cur).ljust(maxWidth)]
    
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
solution = Solution()
print(solution.fullJustify(words, maxWidth))

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(solution.fullJustify(words, maxWidth))