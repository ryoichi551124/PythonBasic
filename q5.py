list1 = [10, 20, 30, 40, 10]
list2 = [10, 20, 30, 40, 50]

def check_list(list):
    if list[0] == list[-1]:
        flug = True
    else:
        flug =  False
    print(f'Given list is {list}')
    print(f'result is {flug}')

check_list(list1)
check_list(list2)