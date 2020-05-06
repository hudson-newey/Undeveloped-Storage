usernameMaster = "grathium"
passwordMaster = "admin1234"

def Program
    puts "Logged In!"
end

puts "Username:"
usrname = gets.chomp
puts "Password:"
pswd = gets.chomp

if (usrname == usernameMaster && pswd == passwordMaster) then
    Program()
else
    puts "Incorrect..."
end