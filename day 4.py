first_range = 264360
second_range = 746325
password_try = [2, 6, 4, 3, 6, 0]
password_result = []
i = 0


def check_decrease():
    if password_try[0] <= password_try[1] <= password_try[2] <= password_try[3] <= password_try[4] <= password_try[5]:
        return False
    else:
        return True


def check_size():
    if password_try.count(0) == 2:
        return True
    elif password_try.count(1) == 2:
        return True
    elif password_try.count(2) == 2:
        return True
    elif password_try.count(3) == 2:
        return True
    elif password_try.count(4) == 2:
        return True
    elif password_try.count(5) == 2:
        return True
    elif password_try.count(6) == 2:
        return True
    elif password_try.count(7) == 2:
        return True
    elif password_try.count(8) == 2:
        return True
    elif password_try.count(9) == 2:
        return True
    else:
        return False




def check_adjacent():
    if password_try[0] == password_try[1] or password_try[1] == password_try[2] or password_try[2] == password_try[3] or \
            password_try[3] == password_try[4] or password_try[4] == password_try[5]:
        if check_size():
            return True
    else:
        return False


def check_password():
    if not check_decrease():
        if check_adjacent():
            print("This password is good " + str(password_try))
            password_result.append(1)


def increase_value():
    if password_try[5] == 9:
        password_try[5] = 0

        if password_try[4] >= 9:
            password_try[4] = 0

            if password_try[3] == 9:
                password_try[3] = 0

                if password_try[2] == 9:
                    password_try[2] = 0

                    if password_try[1] == 9:
                        password_try[1] = 0

                        if password_try[0] == 9:
                            password_try[0] = 0
                        else:
                            password_try[0] += 1
                    else:
                        password_try[1] += 1
                else:
                    password_try[2] += 1
            else:
                password_try[3] += 1
        else:
            password_try[4] += 1
    else:
        password_try[5] += 1


while i < second_range - first_range:
    check_password()
    increase_value()
    i += 1

print(len(password_result))
print(len(password_try))
