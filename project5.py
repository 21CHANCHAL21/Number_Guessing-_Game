# Password strength Checker

lower_count = upper_count = num_count = wspace_count = special_count = 0
s = input()

if (len(s) >= 8):
    for i in s:
        if (i.islower()):
            lower_count += 1
        elif (i.isupper()):
            upper_count += 1
        elif (i.isdigit()):
            num_count += 1
        elif (i == "_"):
            wspace_count += 1

        else:
            special_count += 1

    if (lower_count >= 1 and upper_count >= 1 and num_count >= 1 and wspace_count >= 1 and special_count >= 1):
        print("Password is Valid")
    else:
        print("Invalid Password")

else:
    print("Password is Invalid The length of the Password should be grater than 8 or equal to 8")