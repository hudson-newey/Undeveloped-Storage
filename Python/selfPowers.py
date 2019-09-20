print("Number to count to:")
max = int(input())
max += 1

sum = 0
for p in range(max):
    sum += (p**p)
sum -= 1
print(str(sum)[-10:])