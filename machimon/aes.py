import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import uuid
import requests
import json

class AESCipher(object):
    """
    Verbatim from https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
    
    """
    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


secure = AESCipher(str(uuid.uuid4()))
data = requests.get("http://api.imindus.net/v1/lc/loans/id/57244345").json()[0]
secured = secure.encrypt(json.dumps(data))
secured_string = str(secured, encoding='utf-8')
print(secured_string)
print(secure.decrypt(secured_string))