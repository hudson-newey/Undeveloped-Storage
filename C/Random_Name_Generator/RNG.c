#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main() {
  FILE *fp;
  int names;
  char line[256];
  char sFileOutput[1028];
  char c;

  // make array of names list
  const char *files[2];
  files[0] = "first.txt";
  files[1] = "last.txt";

  for (size_t set = 0; set <= 1; set++) {
    fp = fopen(files[set], "r");

    // Extract characters from file and store in character c
    names = 0;
    for (c = getc(fp); c != EOF; c = getc(fp)) {
      if (c == '\n') { // Increment count if this character is newline
          names++;
      }
    }
    fclose(fp);

    // get a random number for the name
    srand(time(NULL));
    int tempi = rand() % names;

    // gets the first name from file
    fp = fopen(files[set], "r");
    for (size_t i = 0; i < tempi; i++) {
      fscanf(fp, "%s", sFileOutput);
    }
    printf("%s ", sFileOutput); // print first name
    fclose(fp);
  }
  printf("\n");
}
