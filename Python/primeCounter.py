prime = 0

print("Number to get,")
limit = int(input())
limit += 1
failed = False

i = 0
primesFound = 0
while primesFound <= limit:
    failed = False
    for testing in range(i):
        if testing == 0 or testing == 1: continue

        # if it is divisable keep going
        if i % testing == 0:
            failed = True
            break

        # end of loop and therefore it is a prime
    if (failed == False):
        prime = i
        primesFound += 1
    i += 1

print("\nAnswer: ", prime)