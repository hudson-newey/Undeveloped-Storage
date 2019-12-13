package main
import (
	"fmt"
	"math/rand"
	"time"
	"os"
	"os/exec"
	)

func main() {
	// change the color of the console
	cmd := exec.Command("cmd", "/c", "color 2")
	cmd.Stdout = os.Stdout
	cmd.Run()
	
	for ok := true; ok; ok = true {
		rand.Seed(time.Now().UTC().UnixNano())
		fmt.Print(randomString(1)) // print out the random charicter
	}
}

// function to print out a random charicter
func randomString(l int) string {
    bytes := make([]byte, l)
    for i := 0; i < l; i++ {
        bytes[i] = byte(randInt(65, 90))
    }
    return string(bytes)
}

func randInt(min int, max int) int {
    return min + rand.Intn(max-min)
}
