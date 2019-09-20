#include <stdio.h>
#include <stdlib.h>

int main() {
  char name[128];

  printf("What's your Name? ");
  scanf("%s", name);
  printf("Hello, %s!\n", name);

  return 0;
}
