#!/bin/bash

printf "File to build: ";
read file;
g++ $file `pkg-config gtkmm-3.0 --cflags --libs`;
printf "\nDone!\n";
