# chess game
#
# if we started off with 1 grain of rice and kept doubling the amount of rice for
# every chess square
# how many grains of rice would there be

total = 1
print("1 : 1")
for i in range(63):
    total *= 2
    print(str(i + 2) + " : " + str(total))

print("\nTotal:  " + total)