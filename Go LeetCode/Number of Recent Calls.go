package main

type RecentCounter struct {
	s []int
}

func Constructor() RecentCounter {
	return RecentCounter{}
}

func (rc *RecentCounter) Ping(t int) (i int) {
	rc.s = append(rc.s, t)
	for _, c := range rc.s {
		if c+3000 >= t {
			break
		}
		i++
	}
	rc.s = rc.s[i:]
	return len(rc.s)
}
