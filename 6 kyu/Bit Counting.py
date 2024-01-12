def count_bits(n):
    return sum(1 for i in to_binary(n) if i == '1')


def to_binary(n):
    binary_n = ""
    while n != 0:
        binary_n += str(n % 2)
        n //= 2
    return binary_n


print(len(to_binary(1234))//2)
