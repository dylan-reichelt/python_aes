# python_aes
An AES Encryption/Decryption program. This uses the standard 128 bit aes encryption.

## Installation
Make sure you have Numpy installed. If you're unsure how to do that go here: https://scipy.org/install.html


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

NOTE: This will automatically handle any conversions of strings, as well as the 16 byte limit
of AES is handled as well within. So the text can be greater than 16bytes the encryption and
decryption will handle that. The key MUST be 16 bytes however.


```python
from aes_encryption import aes

aesBody = aes("general dynamics")

inputText = sys.argv[1]

aesBody = aes("general dynamics")
cypherText = aesBody.encrypt(inputText)
print("Encrypted Text: ", cypherText)
plaintext = aesBody.decrypt(cypherText)
print("Decrypted Text: ", plaintext)
```

## Contributing
Honestly, I won't be working on this too much as it was made as a working test for my Capstone Project. However, if you wish make changes go for it and I will review them when I have time!

## License
[MIT](https://choosealicense.com/licenses/mit/)
