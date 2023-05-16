class Solution:
    def isValid(self, s: str) -> bool:
        z = []
        p = {"]": "[",
            "}": "{",
            ")": "("}
        for i in s:
            if i in {"(", "[", "{"}:
                z.append(i)
            elif not z:
                return False
            elif z[-1] == p[i]:
                z.pop()
            else:
                return False
        return False if z else True


print(Solution().isValid("()"))
print(Solution().isValid("(]"))
