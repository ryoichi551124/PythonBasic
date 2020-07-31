print('Printing current and previous number sum in a given range(10)')

for i in range(10):
    current = i
    previous = i - 1
    if previous <= 0:
        previous = 0
    sum = current + previous

    print(f'Current Number {current} Previous Number {previous} Sum: {sum}')


