# finds the first fibonacci number with 1000 charicters in it
num1 = 1
num2 = 2
num3 = num1 + num2

# start at 4 because 3 numbers have automaticly been allocated
# and idex's in python start at 3
index = 4
while len(str(num3)) < 1000:
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    index += 1

print(index)