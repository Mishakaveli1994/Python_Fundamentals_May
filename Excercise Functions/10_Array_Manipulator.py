entry_array = [int(i) for i in input().split(' ')]


def exchange(array, index):
    return array[index + 1:] + array[:index + 1]


def max_num(array, subreq):
    if subreq == 'even':
        max_elem = [int(i) for i in array if i % 2 == 0]
        if len(max_elem) == 0:
            return 'No matches'
        else:
            max_elem = max(max_elem)
            return len(array) - 1 - array[::-1].index(max_elem)
    elif subreq == 'odd':
        max_elem = [int(i) for i in array if i % 2 != 0]
        if len(max_elem) == 0:
            return 'No matches'
        else:
            max_elem = max(max_elem)
            return len(array) - 1 - array[::-1].index(max_elem)


def min_num(array, subreq):
    if subreq == 'even':
        min_elem = [int(i) for i in array if i % 2 == 0]
        if len(min_elem) == 0:
            return 'No matches'
        else:
            min_elem = min(min_elem)
            return len(array) - 1 - array[::-1].index(min_elem)
    elif subreq == 'odd':
        min_elem = [int(i) for i in array if i % 2 != 0]
        if len(min_elem) == 0:
            return 'No matches'
        else:
            min_elem = min(min_elem)
            return len(array) - 1 - array[::-1].index(min_elem)


def first_count(array, count, subreq):
    if len(array) < count:
        return 'Invalid count'
    else:
        new_arr = []

        if subreq == "odd":
            for i in range(len(array)):
                if array[i] % 2 != 0 and count > 0:
                    new_arr.append(array[i])
                    count -= 1
        elif subreq == "even":
            for i in range(len(array)):
                if array[i] % 2 == 0 and count > 0:
                    new_arr.append(array[i])
                    count -= 1

        return new_arr


def last_count(array, count, subreq):
    if len(array) < count:
        return 'Invalid count'
    else:
        if subreq == 'even':
            all_nums = [i for i in array if i % 2 == 0]
            if len(all_nums) == 0:
                return []
            else:
                if len(all_nums) < count:
                    return all_nums
                else:
                    return all_nums[len(all_nums) - count:]

        elif subreq == 'odd':
            all_nums = [i for i in array if i % 2 != 0]
            if len(all_nums) == 0:
                return []
            else:
                if len(all_nums) < count:
                    return all_nums
                else:
                    return all_nums[len(all_nums) - count:]


def solution(array, command):
    global entry_array
    command_split = command.split(' ')
    if command_split[0] == 'exchange':
        split_index = int(command_split[1])
        if split_index < 0 or split_index >= len(array):
            print("Invalid index")
        else:
            entry_array = exchange(entry_array, split_index)
    elif command_split[0] == 'max':
        print(max_num(array, command_split[1]))
    elif command_split[0] == 'min':
        print(min_num(array, command_split[1]))
    elif command_split[0] == 'first':
        print(first_count(array, int(command_split[1]), command_split[2]))
    elif command_split[0] == 'last':
        print(last_count(array, int(command_split[1]), command_split[2]))


while True:
    command = input()
    if command == 'end':
        print(entry_array)
        break
    else:
        solution(entry_array, command)
