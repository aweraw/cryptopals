from Crypto.Cipher import AES
from base64 import decodebytes

key = b"YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)

b64_data = open('7.txt', 'rb').read()
data = cipher.decrypt(decodebytes(b64_data))
print(''.join(chr(b) for b in data))
