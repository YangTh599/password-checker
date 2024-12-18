import os
from os.path import join

VALID_CHARS = "abcdefghijklmnopqrstuvxyz0123456789"

def check_first_five(password):
    if check_pass_length(password,4)  and password[:5].isalpha():
        return True
    else:
        return False
    
def check_last_three(password):
    if check_pass_length(password, 2) and password[-3:].isdigit():
        return True
    else:
        return False
    
def check_pass_length(password, l=8):
    if len(password) > l:
        return True
    else:
        return False
    
def check_digit_and_letters(password):
    if password.isalpha():
        return False
    elif password.isdigit():
        return False
    elif check_specials(password):
        return False
    else:
        return True
    
def check_specials(password):
    for char in password:
        if char not in VALID_CHARS:
            return True
    return False

# valid_imgs = ('wait.png', 'yes.png', 'no.png')
ad_imgs = ["thayerad.png"]

# for img in valid_imgs:
#     print(os.path.exists(join('password_assets', 'validation_imgs', img)))

for img in ad_imgs:
    print(os.path.exists(join('password_assets', 'ads', img)))

# print(check_first_five("jdsss"))
# print(check_last_three("3g344"))
# print(check_digit_and_letters("asdasd$$345345"))