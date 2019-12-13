#include <iostream>
#include <string.h>
using namespace std;

void program() {
    // actuall program to run
}



int main() {
    const char username[128] = "admin";
    const char password[128] = "admin1234";

    char usr[128];
    char pswd[128];

    std::cout << "Username:" << endl << ">";
    std::cin >> usr;
    std::cout << "Password:" << endl << ">";
    std::cin >> pswd;

    // compare the usernames and passwords
    if (strcmp(usr, username) == 0 && strcmp(pswd, password) == 0) {
        std::cout << "Logged in!" << endl;
        program();
    }
    
    return 0;
}