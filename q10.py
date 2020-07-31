first_list = [10, 20, 23, 11, 17]
second_list = [13, 43, 24, 36, 12]

odd_list = []
even_list = []

for i in first_list:
    if i % 2 != 0:
        odd_list.append(i)

for i in second_list:
    if i % 2 == 0:
        even_list.append(i)

result_list = odd_list + even_list

print(f'First List {first_list}')
print(f'Second List {second_list}\n')
print(f'result List is {result_list}')