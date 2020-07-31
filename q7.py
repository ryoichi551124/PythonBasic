def string_count(string, target):
    count = string.count(target)
    print(f'{target} appeared {count} times')

test_string = 'Emma is good developer. Emma is a writer'

string_count(test_string, 'Emma')