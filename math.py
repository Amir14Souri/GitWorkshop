def prime(n):
    if n < 10:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return False

print(is_prime(17))  # True
print(is_prime(20))  # False
