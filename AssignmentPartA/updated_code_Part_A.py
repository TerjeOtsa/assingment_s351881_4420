def find_prime_factors(n, prime_factors=None):
    if prime_factors is None:
        prime_factors = []
    
    # Handle factors of 2 separately
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    
    # Now n is odd, so we can skip even numbers
    i = 3
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 2  # Increment by 2, only check odd numbers
    
    if n > 1:
        prime_factors.append(n)
    
    return prime_factors

print(find_prime_factors(1))    # Expected output: []
print(find_prime_factors(56))   # Expected output: [2, 2, 2, 7]
print(find_prime_factors(97))   # Expected output: [97] (since 97 is a prime number)
print(find_prime_factors(100))  # Expected output: [2, 2, 5, 5]
print(find_prime_factors(8688)) # Expected output: [2, 2, 2, 2, 3, 181]
print(find_prime_factors(8689)) # Expected output: [8689] (since 8689 is a prime number)
