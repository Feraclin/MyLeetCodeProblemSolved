class FrontMiddleBackQueue:

    def __init__(self):
        from collections import deque
        self.l = deque()
        self.r = deque()

    def pushFront(self, val: int) -> None:
        self.l.appendleft(val)
        print(self.l, self.r)

    def pushMiddle(self, val: int) -> None:
        self.reb()
        self.l.append(val)
        print(self.l, self.r)

    def pushBack(self, val: int) -> None:
        self.r.append(val)
        print(self.l, self.r)

    def popFront(self) -> int:
        self.reb()
        if len(self.l) == 0:
            return self.popMiddle()
        return self.l.popleft()

    def popMiddle(self) -> int:
        self.reb()
        if len(self.r) == 0:
            return -1
        elif len(self.l) == len(self.r):
            return self.l.pop()
        else:
            return self.r.popleft()

    def popBack(self) -> int:
        self.reb()
        if len(self.r) == 0:
            return -1
        return self.r.pop()

    def reb(self) -> None:
        if len(self.l) == len(self.r) or len(self.l) + 1 == len(self.r):
            return
        elif len(self.l) > len(self.r):
            self.r.appendleft(self.l.pop())
            return self.reb()
        else:
            self.l.append(self.r.popleft())
            return self.reb()


q = FrontMiddleBackQueue()
q.pushFront(1)
q.pushFront(2)
q.pushFront(3)
q.pushFront(4)
print(q.popBack())
print(q.popBack())
print(q.popBack())
print(q.popBack())
# q.pushFront(1)  # ;   // [1]
# q.pushBack(2)  # ;    // [1, 2]
# q.pushMiddle(3)  # ;  // [1, 3, 2]
# q.pushMiddle(4)  # ;  // [1, 4, 3, 2]
# print(q.popFront())  # ;     // return 1 -> [4, 3, 2]
# print(q.popMiddle())  # ;    // return 3 -> [4, 2]
# print(q.popMiddle())  # ;    // return 4 -> [2]
# print(q.popBack())  # ;      // return 2 -> []
# print(q.popFront())  # ;     // return -1 -> [] (The queue is empty)
