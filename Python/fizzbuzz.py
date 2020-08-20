def fizzbuzz(n):
    final = ""
    if (n % 5 == 0): final += "fizz"
    if (n % 15 == 0): final += "buzz"
    return (final, n)[final == ""]

print(fizzbuzz(int(input())))