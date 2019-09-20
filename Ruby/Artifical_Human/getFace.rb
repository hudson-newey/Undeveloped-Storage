#!/usr/bin/env ruby
require "open-uri"

puts "Amount of faces to get,"
@amount = gets.chomp.to_i
i = 0

while i < @amount
  # get face
  puts "Getting: #{i}"
  open("https://thispersondoesnotexist.com/image") do |image|
    File.open("./faces/person#{i}.png", "wb") do |file|
      file.write(image.read)
    end
  end

  i += 1
end
