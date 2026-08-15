def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
        
    # Sieve of Eratosthenes
    # Initialize an array of booleans to track prime status
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # We only need to check up to the square root of n
    # because if a number has a factor larger than its square root,
    # the other factor must be smaller than the square root (which we've already checked).
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            # Mark all multiples of p as False, starting from p*p
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False
                
    return sum(is_prime)

def mySqrt(x: int) -> int:
    if x < 2:
        return x
        
    # Binary Search Approach
    # The square root of x must lie between 2 and x // 2
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
            
    # If we didn't find an exact match, the integer square root is the 'right' pointer
    return right
