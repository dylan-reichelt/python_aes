import sys
from aes_encryption import aes

def main():
    inputText = sys.argv[1]
    binaryInput = inputText.encode("utf-8")
    hexInput = binaryInput.hex()

    #aesBody = aes("general dynamics")
    aesBody = aes("Thats my Kung Fu")
    cypherText = aesBody.encrypt(hexInput)
    aesBody.decrypt(cypherText)
    


if __name__ == '__main__':
    main()
