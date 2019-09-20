/*
Copyright (C) 2018 Grathium Industries <grathiumsoftwears@gmail.com>
	This program comes with ABSOLUTELY NO WARRANTY
	This is a free software, and you are welcome to redistribute it under certain
	conditions.
*/

package main

import (
  "fmt"
)

var factVal uint64 = 1
func main()  {
  var n int

  fmt.Scanln(&n)

  fmt.Println("Factorial of", n ,"is", factorial(n))
}

/*     factorial function      */
func factorial(n int) uint64 {
  if(n < 0){
      fmt.Print("Factorial of negative number doesn't exist!")
  }else{
      for i:=1; i<=n; i++ {
        factVal *= uint64(i)  // mismatched types int64 and int
      }

  }
  return factVal  /* return from function*/
}
