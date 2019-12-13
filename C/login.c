#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void program() {
    // actuall program to run
}



int main() {
    const char username[128] = "admin";
    const char password[128] = "admin1234";

    char usr[128];
    char pswd[128];

    printf("Username:\n");
    scanf("%s", usr);
    printf("Password:\n");
    scanf("%s", pswd);

    // compare the usernames and passwords
    if (strcmp(usr, username) == 0 && strcmp(pswd, password) == 0) {
        printf("Logged in!");
        program();
    } else { printf("Incorrect!"); }

    return 0;
}