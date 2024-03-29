package main

func checkInclusion(s1 string, s2 string) bool {
	// Создаем массив `need`, который содержит количество вхождений каждой буквы в строке `s1`.
	need := [26]int{}
	for i := range s1 {
		need[s1[i]-'a']++
	}

	// Создаем массив `have`, который содержит количество вхождений каждой буквы в текущем окне размера `len(s1)` строки `s2`.
	have := [26]int{}
	for r := range s2 {
		// Если размер текущего окна больше, чем `len(s1)`, уменьшаем количество вхождений буквы, которая вышла за пределы окна.
		if r >= len(s1) {
			have[s2[r-len(s1)]-'a']--
		}
		// Увеличиваем количество вхождений текущей буквы.
		have[s2[r]-'a']++
		// Если массивы `need` и `have` равны, то строка `s1` является перестановкой строки `s2`.
		if need == have {
			return true
		}
	}
	// Если не найдено перестановки, возвращаем `false`.
	return false
}
