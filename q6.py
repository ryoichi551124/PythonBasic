list = [10, 20, 33, 46, 55]

print(f'Given list is {list}')
print(f'Divisible of {len(list)} in a list')

for list_number in list:
    if list_number % 5 == 0:
        print(list_number)