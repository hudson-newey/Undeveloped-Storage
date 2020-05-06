package main

import (
	"fmt"
	"bufio"
	"os"
)

func main() {
	// initilization
	usernameMaster := "administrator"
	passwordMaster := "admin1234"

	fmt.Println("Username:")
	usrname := readLine()
	fmt.Println("Password:")
	pswd := readLine()

	if (usrname == usernameMaster && pswd == passwordMaster) {
		program()
	} else {
		fmt.Println("\nIncorrect...")
	}
}

func readLine() string {
	var text string
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	text = scanner.Text()
	return text
}

func program() {
	fmt.Println("\nLogged In!")
}