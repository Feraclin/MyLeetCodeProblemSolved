package main

import "strconv"

func compress(chars []byte) int {
	var tmp int
	tmpC := chars[0]
	writeIdx := 0

	for _, c := range chars {
		if c == tmpC {
			tmp++
		} else {
			chars[writeIdx] = tmpC
			writeIdx++
			if tmp > 1 {
				tmpStr := strconv.Itoa(tmp)
				copy(chars[writeIdx:], tmpStr)
				writeIdx += len(tmpStr)
			}
			tmpC = c
			tmp = 1
		}
	}
	chars[writeIdx] = tmpC
	writeIdx++
	if tmp > 1 {
		tmpStr := strconv.Itoa(tmp)
		copy(chars[writeIdx:], tmpStr)
		writeIdx += len(tmpStr)
	}

	return writeIdx
}
