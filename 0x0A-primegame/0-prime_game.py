#!/usr/bin/python3
"""Prime Game
"""


def sieve(n):
    """Uses the Sieve of Eratosthenes to find all primes <= n"""
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] is True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def prime_count_up_to(n, primes):
    """Returns the count of primes up to n"""
    return sum(1 for p in primes if p <= n)


def isWinner(x, nums):
    """Returns name of the player that won the most rounds,
    where x is the number of rounds and
    nums is an array of n"""
    if not nums or x < 1:
        return None

    max_num = max(nums)
    primes = sieve(max_num)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = prime_count_up_to(n, primes)
        # Maria wins if the number of primes is odd, Ben wins if even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
