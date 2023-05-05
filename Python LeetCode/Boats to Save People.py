class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        boat = 0
        from collections import deque
        deq = deque(sorted(people))
        while len(deq) > 0:
            if len(deq) > 1 and deq[0] + deq[-1] <= limit:
                boat += 1
                deq.popleft()
                deq.pop()
            else:
                boat += 1
                deq.pop()
        return boat

lst = [3,2,2,1]
s = Solution()
b = s.numRescueBoats(lst, 3)
print(b)

lst = [1,2]
s = Solution()
b = s.numRescueBoats(lst, 3)
print(b)

lst = [3,5,3,4]
s = Solution()
b = s.numRescueBoats(lst, 5)
print(b)
