with open("primes/primes_1000.txt", "r") as file:
    primes_1000 = list(map(int, file.readlines()[0].split(",")))

with open("primes/primes_1000000.txt", "r") as file:
    primes_1000000 = list(map(int, file.readlines()[0].split(",")))