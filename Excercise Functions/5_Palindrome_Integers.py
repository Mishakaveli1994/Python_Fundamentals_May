def palindrome_num(list_of_num):
    for i in list_of_num:
        if i == i[::-1]:
            print('True')
        else:
            print('False')


list_of_nums = input().split(', ')

palindrome_num(list_of_nums)
