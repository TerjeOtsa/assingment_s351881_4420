def find_prime_factors(n, prime_factors=[]):
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i += 1
    if n > 1:
        prime_factors.append(n)
    return prime_factors


print(find_prime_factors(1))    # Expected output: [] given output: []
print(find_prime_factors(56))   # Expected output: [2, 2, 2, 7] given output: [2, 2, 2, 7]
print(find_prime_factors(97))   # Expected output: [97] (since 97 is a prime number) given output: [2, 2, 2, 7, 97]
print(find_prime_factors(100))  # Expected output: [2, 2, 5, 5] given output: [2, 2, 2, 7, 97, 2, 2, 5, 5]
print(find_prime_factors(8688)) # Expected output: [2, 2, 2, 2, 3, 181] given output: [2, 2, 2, 7, 97, 2, 2, 5, 5, 2, 2, 2, 2, 3, 181] 
print(find_prime_factors(8689)) # Expected output: [8689] (since 8689 is a prime number) given output: [2, 2, 2, 7, 97, 2, 2, 5, 5, 2, 2, 2, 2, 3, 181, 8689]
