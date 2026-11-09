"""Prime factorization of a positive integer."""


def factorize(number):
    if not isinstance(number, int) or isinstance(number, bool) or number < 1:
        raise ValueError('Expected a positive integer')
    factors = []
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors.append(divisor)
            number //= divisor
        divisor += 1
    if number > 1:
        factors.append(number)
    return factors


if __name__ == '__main__':
    print(*factorize(int(input())))
