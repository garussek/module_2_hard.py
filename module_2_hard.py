n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def get_password(number):
    password = " "
    for i in range(1, number):
         for a in range(1, number):
            if i <= a:
                continue
            elif number % (a + i) == 0:
                password += str(i) + str(a)
    return password
new_number = int(input(" любоe число n:"))
result = get_password(new_number)
print(new_number, "подобран пароль:", result)
