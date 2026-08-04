import string


def has_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def has_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def has_number(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def has_special_character(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def calculate_score(password):
    score = 0

    if has_uppercase(password):
        score += 1
    if has_lowercase(password):
        score += 1
    if has_number(password):
        score += 1
    if has_special_character(password):
        score += 1
    if len(password) >= 12:
        score += 1
    return score


def announcement_of_results(score):
    if score <= 2:
        return "Weak 🔴"

    elif score <= 4:
        return "Medium 🟡"

    return "Strong 🟢"


def check_password_strength(password):
    score = calculate_score(password)
    result = announcement_of_results(score)

    print(result)


def user_password():
    while True:
        password = input("enter your password : ")
        if len(password) < 8:
            print("Please choose your password again and enter at least 8 characters.")
        else:
            check_password_strength(password)
            break


user_password()
