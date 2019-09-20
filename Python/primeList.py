primes = []

print("Max Numbers to test,")
limit = int(input())
limit += 1
failed = False

for i in range(limit):
    failed = False
    for testing in range(i):
        if testing == 0 or testing == 1: continue

        # if it is divisable keep going
        if i % testing == 0:
            failed = True
            break

        # end of loop and therefore it is a prime
    if (failed == False):
        primes.append(i)

del primes[0] # remove 0 from table
del primes[0] # remove 1 from table
print(primes)
