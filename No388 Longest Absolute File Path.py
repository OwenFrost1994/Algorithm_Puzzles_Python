class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lines = input.split("\n")
        stack = [] # [level, cum_size]
        result = 0
        for line in lines:
            if not stack:
                level = line.count("\t")
                stack.append([level, len(line) - level]) # len(line) - level record the length of the string \tsubdir1 is /subdir1 in dir length
            else:
                level = line.count("\t")
                while stack and stack[-1][0] >= level:
                    stack.pop()
                offset = stack[-1][1] + 1 if stack else 0
                stack.append([level, offset + len(line) - level])
            if "." in line:
                result = max(result, stack[-1][1])
        return result


solution = Solution()
print(solution.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))
print(solution.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"))
print(solution.lengthLongestPath(input = "a"))