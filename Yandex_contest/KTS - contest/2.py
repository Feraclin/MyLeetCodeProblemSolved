def substring(s: str) -> int:
    c, t = 0, ''
    for i in s:
        if i in t:
            c = len(t) if len(t) > c else c
            t = t[t.index(i) + 1:]
        t += i
    return len(t) if len(t) > c else c


assert(substring("abc")==3)
assert(substring("aaaaaaa")==1)
assert(substring("abcabc")==3)
assert(substring("dfda")==3)