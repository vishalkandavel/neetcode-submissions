class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for path in path.split('/'):

            if path == "" or path == ".":
                continue

            elif path == "..":
                if stack:
                    stack.pop()

            else:
                stack.append(path)

        return "/" + "/".join(stack)

