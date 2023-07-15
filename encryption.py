import atexit
from cryptography.fernet import Fernet



def encrypt(cipher,fname:str):
    
    print("Encrypting data...")
    # Read the contents of the input file
    with open(fname, 'rb') as file:
        data = file.read()

    # Encrypt the data
    encrypted_data = cipher.encrypt(data)

    # Write the encrypted data to an output file
    with open(fname, 'wb') as file:
        #delete the old data
        file.truncate(0)
        file.write(encrypted_data)


def decrypt(cipher,fname:str):
    
    print("Decrypting data...")
    # Read the contents of the input file
    with open(fname, 'rb') as file:
        data = file.read()

    # Encrypt the data
    decrypted_data = cipher.decrypt(data)
    return decrypted_data

def set_password(password:str):
    global global_password
    global_password = password
    with open("data.txt", "a") as file:

        #decrypt the data
        data = decrypt(cipher,'data.txt').decode()
        file.truncate(0)
        file.write(data)
        file.write("p"+password)
        file.write("\n")
    file.close()
    encrypt(cipher,'data.txt')


with open("private_key.txt", "rb") as file:
    key = file.read()
    if key == b'':
        print("Key not found, generating new key...")
        key = Fernet.generate_key()
        encrypt(Fernet(key),'data.txt')
file.close()


cipher = Fernet(key)



def save_key_on_exit(k):
    with open("private_key.txt", "wb") as file:
        file.write(k)


atexit.register(save_key_on_exit, key)