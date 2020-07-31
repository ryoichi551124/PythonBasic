def exponent(base, exp):
    exponent = base ** exp
    print(f'{base} raises to the power of {exp} is: {exponent} i.e.(', end='')
    print(f'{base}*' * (exp - 1) + f'{base} = {exponent})')

exponent(2, 5)
exponent(5, 4)