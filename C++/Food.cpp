#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main(int argc, char const *argv[]) {
  srand(time(0)); // Initialize random number generator.
  char foods[][255] = {"Cheese Burger", "Chicken Burger", "Pie", "Sausage Roll"};
  char sides[][255] = {"Churros", "Chips"};
  char drinks[][255] = {"NONE"};
  char UserItem[255];

  for (size_t i = 0; i < 3; i++) {

    if (i == 0) { /* MAINS */
      int num_elements = sizeof( foods ) / sizeof( foods[0] );
      int selected = (rand() % num_elements) + 1; // pick a random item from the list
      UserItem = foods[selected];
    } else if (i == 1) { /* SIDES */
      int num_elements = sizeof( sides ) / sizeof( sides[0] );
      int selected = (rand() % num_elements) + 1; // pick a random item from the list
      UserItem = sides[selected];
    } else if (i == 2) { /* DRINKS */
      int num_elements = sizeof( drinks ) / sizeof( drinks[0] );
      int selected = (rand() % num_elements) + 1; // pick a random item from the list
      UserItem = drinks[selected];
    }

    std::cout << UserItem << '\n'; // output what the user got
  }
  return 0;
}
