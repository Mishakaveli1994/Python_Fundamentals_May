number = input()

def off_even_sum(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return odd_sum, even_sum


odd_sum, even_sum = off_even_sum(number)

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
