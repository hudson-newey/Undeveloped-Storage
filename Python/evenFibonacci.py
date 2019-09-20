num1 = 1
num2 = 2
num3 = num1 + num2
thing = [1, 2]

while num3 < 4000000:
    thing.append(num3)
    num1 = num2
    num2 = num3
    num3 = num1 + num2

sum = 0
for i in range(len(thing)):
    if (thing[i] % 2 == 0):
        sum += thing[i]
print(sum)