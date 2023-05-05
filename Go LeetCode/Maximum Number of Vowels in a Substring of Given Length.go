package main

import "strings"

// Функция maxVowels принимает на вход строку s и целочисленный параметр k.
// Она возвращает максимальное количество гласных букв, которые можно найти в подстроке длиной k символов в строке s.

func maxVowels(s string, k int) int {
	var counter, max int
	vowels := "aeiou"

	// Итерируемся по строке s
	for i, c := range s {
		// Если символ является гласной буквой, увеличиваем счетчик
		if strings.ContainsRune(vowels, c) {
			counter++
		}
		// Если длина подстроки превышает k и первый символ в подстроке является гласной буквой, уменьшаем счетчик на 1
		if i >= k && strings.ContainsRune(vowels, rune(s[i-k])) {
			counter--
		}
		// Если текущее значение счетчика больше максимального, обновляем максимальное значение
		if counter > max {
			max = counter
		}
	}
	// Возвращаем максимальное значение счетчика
	return max
}
