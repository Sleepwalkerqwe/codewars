def is_prime(num):
    count = 0
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            count += 1
    return True if count == 0 else False


print(is_prime(int(input())))
