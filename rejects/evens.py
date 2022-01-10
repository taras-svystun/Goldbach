# This module is searching for any even number which cannot be
# shown as sum of two prime numbers.


# Getting lists of prime numbers.
from get_primes import primes_1000


def get_rejections(bound: int) -> list:
    """
    This function searches for numbers, not showable as sum of two primes.
    """
    rejections = list()
    for i in range(2, bound, 2):
        if not splitable(i):
            rejections.append(i)
    return rejections

def splitable(number: int) -> bool:
    """
    This functions checks whether the number could be shown as sum
    of two primes.
    """
    for i in primes_1000:
        remainders = set()
        for j in primes_1000:
            remainders.add(number - j)

        if i in remainders:
            return True
    return False        

rejs = get_rejections(1000)
print(rejs)