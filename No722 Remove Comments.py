from typing import List

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        # multiline = False
        # results = []
        # for s in source:
        #     if not multiline:
        #         if "//" in s and ("/*" in s and s.index("//") < s.index("/*")):
        #             line = s.split("//")[0]
        #             if len(line) > 0:
        #                 results.append(line)
        #             continue
                
        #         if "/*" in s:
        #             line = s.split("/*")[0]
        #             multiline = True
        #             s = "".join(s.split("/*")[1:])
        #             if "*/" in s:
        #                 line = line + s.split("*/")[1]
        #                 multiline = False
        #                 if len(line) > 0:
        #                     results.append(line)
        #         else:
        #             results.append(s)
        #     else:
        #         if "*/" in s:
        #             line = line + s.split("*/")[1]
        #             multiline = False
        #             if len(line) > 0:
        #                 results.append(line)
        # return results
        res = []
        multi = False
        line = ''
        for s in source:
            i = 0
            while i < len(s):
                if not multi:
                    if s[i] == '/' and i < len(s) - 1 and s[i + 1] == '/':
                        break
                    elif s[i] == '/' and i < len(s) - 1 and s[i + 1] == '*':
                        multi = True
                        i += 1
                    else:
                        line += s[i]
                else:
                    if s[i] == '*' and i < len(s) - 1 and s[i + 1] == '/':
                        multi = False
                        i += 1
                i += 1
            if not multi and line:
                res.append(line)
                line = '' # 注意line重新设置成空字符串的位置
        return res
solution = Solution()
print(solution.removeComments(source = ["a//*b//*c","blank","d/*/e*//f"]) == ["a","blank","d/f"])

print(solution.removeComments(source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"]))
print(solution.removeComments(source = ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"])==["struct Node{","    ","    int size;","    int val;","};"])
# ["struct Node{","    ","    int size;","    int val;","};"]
print(solution.removeComments(source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
print(solution.removeComments(source = ["a/*comment", "line", "more_comment*/b"]))