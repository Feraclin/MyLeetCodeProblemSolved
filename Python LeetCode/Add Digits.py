class Solution:
    def addDigits(self, num: int) -> int | str:
        lst = str(num)
        while len(lst) > 1:
            lst = str(sum(map(int, list(lst))))
        return lst

