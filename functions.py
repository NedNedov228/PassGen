import random

#generate a random password of given length
def generate_password(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-+!@#$*()_"
    password = ""
    for i in range(length):
        password += random.choice(charset)
    return password

