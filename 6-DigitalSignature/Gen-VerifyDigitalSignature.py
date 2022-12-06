from Crypto.PublicKey import RSA
from hashlib import sha512

#generate a 1024-bits RSA key-pair
keyPair = RSA.generate(bits=1024)
print(f"\nPublic key: (n = {hex(keyPair.n)}, e = {hex(keyPair.e)})")
print(f"\nPrivate key: (n = {hex(keyPair.n)}, d = {hex(keyPair.d)})")

#RSA sign the message
msg = 'Welcome to Ruia College'
print(f'\nMessage: {msg}')
hash = int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
signature = pow(hash, keyPair.d, keyPair.n)
print(f'\nSignature: {hex(signature)}')

#RSA verify signature
msg = 'Welcome to Ruia College'
hash = int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
if hash == hashFromSignature:
    print('\nSignature valid')
else:
    print('\nSignature invalid')

#RSA verify signature (tampered msg)
msg = 'Welcome to Ruia College Matunga'
print(f'\nMessage(tampered): {msg}')
hash = int.from_bytes(sha512(msg.encode('utf-8')).digest(), byteorder='big')
hashFromSignature = pow(signature, keyPair.e, keyPair.n)
if hash == hashFromSignature:
    print('\nSignature valid')
else:
    print('\nSignature invalid(tampered)')