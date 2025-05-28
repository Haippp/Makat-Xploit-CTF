from base64 import b64encode
from random import randint

flag = b'mXpCTF{...}'
b64ciper = flag

for i in range(randint(1, 50)):
    b64ciper = b64encode(b64ciper)

open('crazy_cipher.txt', 'a').write(b64ciper.decode())