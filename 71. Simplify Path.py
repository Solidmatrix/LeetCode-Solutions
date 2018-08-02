class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dirs = path.split("/")
        stack = []
        for d in dirs:
            if d == "" or d == ".":
                pass
            elif d == "..":
                if len(stack) != 0:
                    del stack[-1]
            else:
                stack.append(d)
        result = ""
        for s in stack:
            result += "/"
            result += s
        if result == "":
            result += "/"
        return result