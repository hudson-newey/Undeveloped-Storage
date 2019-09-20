#include <stdio.h>
#include <stdlib.h>

void main() {
    FILE *fp;
    char sFilename[128];
    char sFileOutput[1028];

    printf("What File do you want to open: ");
    scanf("%s", sFilename);

    // read the file
    fp = fopen(sFilename, "r");
    while (fscanf(fp, "%s", sFileOutput) != EOF) {
        printf("%s\n", sFileOutput);
    }
    fclose(fp);
}
