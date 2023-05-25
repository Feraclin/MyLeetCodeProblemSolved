package main

func removeStars(s string) string {
	res := make([]rune, 0, len(s))
	for _, v := range s {
		if v == '*' {
			res = res[:len(res)-1]
		} else {
			res = append(res, v)
		}
	}
	return string(res)
}
