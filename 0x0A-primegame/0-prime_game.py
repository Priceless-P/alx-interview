#!/usr/bin/python3

def is_prime(n):
    """Checks whether or not a number is prime"""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5) + 1, 2):
        if n % i:
            return False
    return True


def find_primes(x):
    """Returns the prime numbers in
    given an array of numbers"""
    return [num for num in x if is_prime(num)]


def find_multiples(prime, numbers):
    """Returns multiples of a prime number"""
    return [num for num in numbers if num % prime == 0]


def play_game(sub_list):
    """Returns a winner for each round of game"""
    turn = 0  # Maria's turn is 0, Ben is 1

    # Get primes number in Lists
    primes = find_primes(sub_list)

    # loop through the sublist
    while True:
        # if no more primes in list break
        if not primes:
            break

        # Maria chooses the least prime number
        prime_chosen = primes[0]

        multiples_to_remove = find_multiples(prime_chosen, sub_list)
        sub_list = [num for num in sub_list if num not in multiples_to_remove]
        turn = 1 - turn

        if turn == 0:
            return "Maria"
        else:
            return "Ben"


def isWinner(x, nums):
    """Returns name of the player that won the most rounds,
    where x is the number of rounds and
    nums is an array of n"""
    maria_wins = 0
    ben_wins = 0
    for i in range(x):
        sub_list = list(range(1, nums[i] + 1))
        round_winner = play_game(sub_list)

        if round_winner == "Maria":
            maria_wins += 1
        elif round_winner == "Ben":
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    else:
        return "Ben"
