#!/usr/bin/env ruby
=begin
Labyrinth Copyright (C) 2018 Grathium Sofwares <grathiumsoftwears@gmail.com>
This program comes with ABSOLUTELY NO WARRANTY
This is a free software, and you are welcome to redistribute it under certain
conditions.
=end

puts "Seconds to Count Down From,\n"
TotalSec = gets.chomp.to_i

i = 0
while i < TotalSec do
  system "cls"
  system "clear"
  puts TotalSec - i

  sleep(1)
  i += 1
end
puts "Done!"
