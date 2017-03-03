from string import ascii_letters, digits

valid_values = list(digits + ascii_letters)
radix = len(valid_values)

def convert(number):
    result = []

    while number:
        result.insert(0, valid_values[number % radix])
        number //= radix

    return ''.join(result)


def inverse(number):
    result = 0

    # number = 100500
    # (0, Y) (1, 8) (2, q)
    # p, c = (0, Y) === p, c = 0, Y
    for p, char in enumerate(reversed(number)):
        n = valid_values.index(char)
        result += n * radix ** p

    return result