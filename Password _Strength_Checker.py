import re

def check_password_strength(password):
    # Check the password length
    if len(password) < 8:
        return 0, "Password is too short. It should be at least 8 characters long."

    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return 0, "Password should contain both uppercase and lowercase letters."

    if not re.search(r'\d', password):
        return 0, "Password should contain at least one digit."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return 0, "Password should contain at least one symbol."

    score = 0
    score += len(password) * 4
    score += (len(password) - len(re.sub(r'[a-z]', '', password))) * 2
    score += (len(password) - len(re.sub(r'[A-Z]', '', password))) * 2
    score += len(re.findall(r'\d', password)) * 4
    score += len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) * 6
    if len(password) >= 12:
        score += 10

    if score < 60:
        message = "The password is  VERY WEAK. You could choose a stronger password."
    elif score < 80:
        message = "The password is WEAK.You could choose a stronger password!"
    elif score < 100:
        message = "The password is STROG. You could improve a stronger password!"
    else:
        message = "The password is VERY STROG. Great job!"

    return score, message

while True:
    password = input("Enter your password: ")
    score, message = check_password_strength(password)
    print("Your password strength score is:", score)
    print(message)
    if score >= 80:
        break
    else:
        print("Please enter a stronger  password with a score of at least 80 \n")
