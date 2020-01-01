#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;
int rand();

int randomNumber() {
    return round(rand() / 1000000);
}

void quiz(char method) {
    int answer;
    int num1;
    int num2;
    int guess;

    while (true) {
        num1 = randomNumber();
        num2 = randomNumber();

        switch (method) {
            case 'a':
                answer = num1 + num2;
                std::cout << num1 << "+" << num2 << "=";
                break;
            case 's':
                answer = num1 - num2;
                std::cout << num1 << "-" << num2 << "=";
                break;
            case 'm':
                answer = num1 * num2;
                std::cout << num1 << "*" << num2 << "=";
                break;
            case 'd':
                answer = num1 / num2;
                std::cout << num1 << "/" << num2 << "=";
                break;
        }
        std::cin >> guess;
    
        // check answer
        if (guess == answer) {
            std::cout << "Correct!" << endl;
        } else {
            std::cout << "Incorrect!" << endl;
        }

        // restart
        std::cout << endl;
    }
}

int main(int argc, char const *argv[])
{
    while (true)
    {
        char method;
        std::cout << "Addition, Subtraction, Multiplication or Division?" << endl << ">";
        std::cin >> method;

        method = tolower(method);
        if (!(method == 'a' || method == 's' || method == 'm' || method == 'd')) {
            //opperator not recognised
            std::cout << "Unknown Opperator!" << endl;
            exit;
        }
        quiz(method);
    }
    return 0;
}
