#include <stdio.h>

void main() {
  int a = 19; //set a to 19
  int *pointer = &a; //set pointer to variable a
  a++; //increase by one

  //print variable a
  printf("%i\n", *pointer);
}
