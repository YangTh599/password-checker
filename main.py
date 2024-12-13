# Thayer Yang
# 13 DEC 2024
# Password Checker

def checkAllTrue(bool_list):
    for cond in bool_list:
        if cond == False:
            return False
    return True


password = ''
score = 0

ALPHABET = 'abcdefghijklmnopqrstuwxyz'
NUMS = '0123456789'
SPECIAL_CHARS = '~`! @#$%^&*()_-+={[}]|\:;"\'<,>.?/'
MIN_LENGTH = 8

password = input("Enter in a password:\n")

print()

has_upper = False
has_lower = False
has_special = False
has_nums = False

for char in password:

    if char in ALPHABET: #Checks for lowercase letters
        has_lower = True
    elif char in ALPHABET.upper(): #Checks for uppercase letters
        has_upper = True
    elif char in SPECIAL_CHARS: #Checks for special characters
        has_special = True
    elif char in NUMS: # Checks for Numbers
        has_nums = True
    
    if checkAllTrue([has_upper, has_lower, has_special, has_nums]):
        score += 25
        break


if checkAllTrue([has_upper, has_lower, has_special, has_nums]):
    # This ling only executes if all booleans are true from the previous block of code
    if len(password) >= MIN_LENGTH: # Checks if password is 8 characters long
        score += 5

else:
    if has_upper and has_lower: #Checks if password has upper and lowercase
        score += 10

    if (has_upper or has_lower) and has_nums: #checks if password has letters and numbers
        score += 10 

    if has_special: # Checks if password has special characters
        score +=5

    if len(password) >= MIN_LENGTH: # checks if password is 8 characters long
        score+5

#This Block checks if password has atleast 2 uppercase latters and 2 lowercase letters
if has_lower and has_upper:
        lower_count = 0
        upper_count = 0

        for char in password:
            if char in ALPHABET:
                lower_count += 1
            elif char in ALPHABET.upper():
                upper_count += 1
            
            if lower_count >=2 and upper_count >=2:
                score +=15
                break
    
# This Block checks if the password contains atleast 2 numbers
if has_nums:
    num_count = 0

    for char in password:
        if char in NUMS:
            num_count +=1

        if num_count >= 2:
            score += 15
            break

print(f"Your password:\n{password}\nYour Score: {score}")

print()

if score < 10:
    print("Your password needs serious revisions")
elif score < 20:
    print("Your password does ok but needs a little work")
elif score < 30:
    print("You have a stable password")
elif score < 40:
    print("You have a decent password")
elif score < 50:
    print("You almost have a great password")
elif score >= 50:
    print("You have an amazing password!")
