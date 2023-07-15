import random

#generate a random password of given length
def generate_password(length):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/-+!@#$*()_"
    password = ""
    for i in range(length):
        password += random.choice(charset)
    return password

#copy text to clipboard
def copy_to_clipboard(root,text):
    root.clipboard_clear()
    root.clipboard_append(text)