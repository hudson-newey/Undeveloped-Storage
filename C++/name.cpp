#include <iostream>
using namespace std;

int main()
{
  char name[255];
  std::cout << "What is your name," << endl;
  cout << ">";
  std::cin >> name;

  std::cout << "Hello, " << name << "!" << endl; // Say hello

  return 0;
}