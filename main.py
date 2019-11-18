import sys
from aes_encryption import aes

def main():
    inputText = sys.argv[1]
    binaryInput = inputText.encode("utf-8")
    hexInput = binaryInput.hex()

    aesBody = aes("general dynamics")
    cypherText = aesBody.encrypt(hexInput)
    print("Encrypted Text: ", cypherText)
    plaintext = aesBody.decrypt(cypherText)
    print("Decrypted Text: ", plaintext)
    


if __name__ == '__main__':
    main()
