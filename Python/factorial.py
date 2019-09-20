# finds the a factorial

def factorial(num):
    sum = 1
    for i in range(num):
        if (i == 0): continue
        sum *= i
    return str(sum)

print("Get factorial of:")
print(factorial(int(input()) + 1))