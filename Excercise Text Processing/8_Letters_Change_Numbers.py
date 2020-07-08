strings = (' '.join(input().split())).split(' ')
totalResult = 0


def first_and_last_letter(substr):
    first_letter = substr[0]
    first_letter_ord = ord(first_letter.lower()) - 96
    last_letter = substr[len(substr) - 1]
    last_letter_ord = ord(last_letter.lower()) - 96
    return first_letter, first_letter_ord, last_letter, last_letter_ord


for i in strings:
    endResult = 0
    number = int(i[1:len(i) - 1])
    fl, fl_ord, ll, ll_ord = first_and_last_letter(i)
    if fl.isupper():
        endResult += number/fl_ord
    else:
        endResult += number * fl_ord
    if ll.isupper():
        endResult -= ll_ord
    else:
        endResult += ll_ord
    totalResult += endResult
print(f'{totalResult:.2f}')
