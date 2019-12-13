package main
import (
	"fmt"
	"time"
	"os"
	"os/exec"
	)

var t = 0
func main() {
	for ok := true; ok; ok = true {
		fmt.Println(t)
	
		// waits one second using the variable set as "second_wait" as 1 second
		second_wait := time.Second
		time.Sleep(second_wait)
		cmd := exec.Command("cmd", "/c", "cls")
		cmd.Stdout = os.Stdout
		cmd.Run()
	
		t++
	}
}
