def perfect_number(number):
    sum = 0
    for i in range(1, number + 1):
        if number % i == 0:
            sum += i
    if int(sum / 2) == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


initial_num = int(input())
perfect_number(initial_num)
