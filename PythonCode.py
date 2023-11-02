from cryptography.fernet import Fernet
import rsa


def SymEncry(Message):
    #Symmetric-Key Encrpytion 

    # Making the key 
    key = Fernet.generate_key()

    fernet = Fernet(key)

    # Encrypting the Message
    EncryptMsg = fernet.encrypt(message.encode())
    print(f"Encrypted Message : {EncryptMsg}")

    # Decrypting the message 
    DecryptingMsg = fernet.decrypt(EncryptMsg).decode()
    print(f"Decryped Message : {DecryptingMsg}")

def AsymEncry(Message):
    publicKey, privateKey = rsa.newkeys(200)

    # Encrypting the Message
    EncryptMsg = rsa.encrypt(Message.encode(),publicKey)
    print(f"Encrypted Message : {EncryptMsg}")

    # Decrypting the message 
    DecryptingMsg = rsa.decrypt(EncryptMsg,privateKey).decode()
    print(f"Decryped Message : {DecryptingMsg}")

Flag = True
while Flag:
    
    Message = str(input("Please enter in a message you want to encrypt :"))
    print()

    print("Select your way of encryption!")
    print(" 1 - Symmetric Encrpytion")
    print(" 2 - Asymmetric Encryption\n")
    choice = int(input("Enter :"))
    if choice == 1:
        SymEncry(Message)
    else:
        AsymEncry(Message)
