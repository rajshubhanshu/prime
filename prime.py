def prime_factors(n):
    factors = []
    # Divide by 2 until n is odd
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # Check for odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

# Take input from user
num = int(input("Enter a number:\n"))
result = prime_factors(num)
print("Prime factors:", result)
