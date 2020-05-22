string1 = input()
string2 = input()
new_string = ''
# For the range of the second string we do a loop
for i in range(len(string2)):
    # If the elements are different
    if string1[i] != string2[i]:
        # Add slice string2[:i+1] to string1[i+1:]
        # This would mean string2[string_start:index(i in this case) + 1 (as len starts from 1 not from 0)]
        new_string = string2[:i+1]+string1[i+1:]
        print(new_string)