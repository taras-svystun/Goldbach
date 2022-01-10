from math import sqrt

def get_primes(bound: int) -> set:
    primes = list()
    for i in range(1, bound):

        for j in range(2, int(sqrt(i) + 1)):
            if not i % j:
                break
        else:
            primes.append(i)
    
    return primes

primes_1000000 = get_primes(1000000)
print(primes_1000000)
with open("primes/primes_1000000.txt", "w") as file:
    file.write(", ".join(map(str, primes_1000000)))