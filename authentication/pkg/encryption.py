import base64
from typing import ByteString

from Cryptodome.Cipher import AES
from Cryptodome.Cipher._mode_ecb import EcbMode
from Cryptodome.Util.Padding import pad, unpad

def get_new_cipher(key: ByteString) -> EcbMode:
    return AES.new(key, AES.MODE_ECB)

def ciphertext_encrypt(cipher: EcbMode, data: str) -> ByteString:
    return cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))

def ciphertext_decode(encrypted_data: ByteString) -> bytes:
    try:
        cipher_decode = base64.b64decode(encrypted_data)
    except Exception as e:
        raise ValueError('Invalid encrypted data')
    else:
        return cipher_decode
    
# Encryption 32 bytes
def encrypt(data: str, key: ByteString) -> str:
    cipher = get_new_cipher(key=key)
    ciphertext = ciphertext_encrypt(cipher=cipher, data=data)
    encrypted = base64.b64encode(ciphertext).decode('utf-8')
    return encrypted

def decrypt(encrypted: ByteString, key: ByteString) -> str:
    cipher = get_new_cipher(key=key)
    cipher_text= ciphertext_decode(encrypted_data=encrypted)
    try:
        decrypted_token = unpad(cipher.decrypt(cipher_text), AES.block_size).decode('utf-8')
    except Exception as e:
        raise ValueError(e)
    else:
        return decrypted_token
    
