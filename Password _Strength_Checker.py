import re
import string

def check_password_strength(password):
    # Check the password length
    if len(password) < 8:
        return 0, "Password is too short. It should be at least 8 characters long."

    # Check if the password contains uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return 0, "Password should contain both uppercase and lowercase letters."

    # Check if the password contains digits
    if not re.search(r'\d', password):
        return 0, "Password should contain at least one digit."

    # Check if the password contains symbols
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return 0, "Password should contain at least one symbol."

    # Check if the password is a common password
    with open('common_passwords.txt') as file:
        common_passwords = file.readlines()
        common_passwords = [x.strip() for x in common_passwords]
    if password in common_passwords:
        return 0, "Password is too common. Please choose a different password."

    # Calculate the password strength score
    score = 0
    score += len(password) * 4
    score += (len(password) - len(re.sub(r'[a-z]', '', password))) * 2
    score += (len(password) - len(re.sub(r'[A-Z]', '', password))) * 2
    score += len(re.findall(r'\d', password)) * 4
    score += len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) * 6
    if len(password) >= 12:
        score += 10

    # Return the password strength score and a message
    if score < 20:
        message = "Password is very weak. Please choose a stronger password."
    elif score < 40:
        message = "Password is weak. Please choose a stronger password."
    elif score < 60:
        message = "Password is medium. You could choose a stronger password."
    elif score < 80:
        message = "Password is strong. Good job!"
    else:
        message = "Password is very strong. Great job!"

    return score, message



input = password
print = password 
score, message = check_password_strength(password)
print(f"Password: {password} - Score: {score} - Message: {message}")


input = x