def countPrimes(n: int) -> int:
    """
    Given an integer n, return the number of prime numbers that are strictly less than n.
    Must be solved faster than O(n * sqrt(n)).
    """
    if n <= 2:
        return 0
    
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
    
    return sum(is_prime)

def mySqrt(x: int) -> int:
    """
    Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.
    """
    if x < 2:
        return x
    
    left, right = 2, x // 2

    while left <= right:
        pivot = left + (right - left) // 2
        num = pivot * pivot

        if num > x:
            right = pivot - 1
        elif num < x:
            left = pivot + 1
        else:
            return pivot
        
    return right


def main():
    print("Welcome to Day 36: Math & Number Theory!")
    print("Run `python test_cases.py` to check your implementations.")

if __name__ == "__main__":
    main()
