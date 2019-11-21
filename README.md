# python_aes
An AES Encryption/Decryption program. This uses the standard 128 bit aes encryption.

## Installation

Download the aes_encryption.py. For global imports run these commands:

```bash
python3
import sys
print(sys.path)
```

You should receive a path to something like:

```bash
'/usr/dylan/env/lib/python3.6/site-packages'
```

Drop aes_encryption.py into this. Now you should be able to import it just like anything else.

## Usage

NOTE: The key can only be 16 bytes (16 ascii characters) and same with the text to encrypt or decrypt. If you want to do larger items for encryption you'll have to use a loop of some kind to parse the data into 16 byte chunks.


```python
from aes_encryption import aes

aesBody = aes("general dynamics")

input = b'this is a test'
cypherText = aesBody.encrypt(input.hex())
print("Encrypted Text: ", cypherText)
plaintext = aesBody.decrypt(cypherText)
print("Decrypted Text: ", plaintext)
```

## Contributing
Honestly, I won't be working on this too much as it was made as a working test for my Capstone Project. However, if you wish make changes go for it and I will review them when I have time!


Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
