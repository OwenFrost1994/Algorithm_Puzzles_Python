class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        newpath = []
        for folder in paths:
            if folder == "..":
                if len(newpath) > 0:
                    newpath.pop()
            elif folder not in [".", ""]:
                newpath.append(folder)
        
        return "/" + "/".join(newpath)


solution = Solution()

path = "/home/"
print(solution.simplifyPath(path))

path = "/../"
print(solution.simplifyPath(path))

path = "/home//foo/"
print(solution.simplifyPath(path))