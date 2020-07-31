def reverse_num(num):
    str_num = str(num)
    reversed_num = str_num[::-1]
    print(f'original number {str_num}')
    
    if str_num == reversed_num:
        print('The original and reverse number is the same')
    else:
        print('The original and reverse number is not same')

reverse_num(121)
reverse_num(125)

