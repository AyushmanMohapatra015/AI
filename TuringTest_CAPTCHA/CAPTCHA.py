import random
import string


def create_captcha():

    characters = string.ascii_letters + string.digits
    captcha_text = ""

    for i in range(6):
        captcha_text += random.choice(characters)

    return captcha_text


def verify_user():

    captcha = create_captcha()

    print("CAPTCHA:", captcha)

    user_input = input("Enter the CAPTCHA exactly as shown: ")

    if user_input == captcha:
        print("Verification successful. You appear to be human.")
    else:
        print("Incorrect CAPTCHA. Try again.")


verify_user()
