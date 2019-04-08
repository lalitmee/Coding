package main

import "fmt"

func main() {
	card := "Ace of Spade"
	card = "Hello There Go!"
	fmt.Println(card)
	sum := 0
	for i := 0; i < 10; i++ {
		fmt.Println(i)
		sum += i
	}
	fmt.Println(sum)
}
