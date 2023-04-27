class Solution:
    def partitionString(self, s: str) -> int:
        count = 0
        tmp_lst = []
        for i in s:
            if i not in tmp_lst:
                tmp_lst.append(i)
            else:
                tmp_lst = [i,]
                count += 1
        if len(tmp_lst) != 0:
            count += 1
        return count

s = Solution()
assert(s.partitionString("abacaba") == 4)
assert(s.partitionString("a") == 1)
assert(s.partitionString("ssssss") == 6)
assert(s.partitionString("") == 0)