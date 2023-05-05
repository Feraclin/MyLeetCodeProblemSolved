package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin) // создаем новый сканер для чтения ввода
	scanner.Scan()                        // считываем введенную строку
	str := scanner.Text()                 // сохраняем считанную строку в переменной str
	if isPalindrome(str) {                // проверяем, является ли строка палиндромом
		fmt.Println("Палиндром") // если да, выводим сообщение "Палиндром"
	} else {
		fmt.Println("Нет") // если нет, выводим сообщение "Нет"
	}
}

func isPalindrome(str string) bool {
	runes := []rune(str)                // преобразуем строку в массив рун
	for i := 0; i < len(runes)/2; i++ { // проходим по половине массива рун
		if runes[i] == ' ' { // если текущий символ - пробел, пропускаем его
			continue
		}
		if runes[len(runes)-1-i] == ' ' { // если символ справа - пробел, пропускаем его и уменьшаем индекс i
			i--
			continue
		}
		if runes[i] != runes[len(runes)-1-i] { // если символы не совпадают, возвращаем false
			return false
		}
	}
	return true // если мы дошли до конца цикла, значит, строка является палиндромом, и мы возвращаем true
}
