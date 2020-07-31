def reverse_order(num):
    num_list =[]
    str_num = str(num)
    reverse_num = str_num[::-1]
    for i in reverse_num:
        num_list.append(i)
    sepa_num_list = ' '.join(num_list)

    print(f'"{sepa_num_list}"')


reverse_order(7536)
reverse_order(123)