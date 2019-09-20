#include <iostream>
#include <gtkmm.h>

int main(int argc, char*argv[]) {
  Gtk::Main kit(argc, argv);
  Gtk::Window window;
  Gtk::Button mainBTN;
  Gtk::Main::run(window);
  Gtk::Main::run(mainBTN);
  return 0;
}
