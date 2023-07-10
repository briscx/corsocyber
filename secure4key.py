from flask import Flask, render_template, request
import hashlib
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        algorithm = request.form['algorithm']

        result = ''
        if algorithm == 'MD5':
            result = md5_hash(text)
        elif algorithm == 'SHA-1':
            result = sha1_hash(text)
        elif algorithm == 'SHA-256':
            result = sha256_hash(text)
        elif algorithm == 'AES':
            key = generate_key()
            result = encrypt_message(text, key)
        elif algorithm == 'RSA':
            private_key, public_key = generate_key_pair()
            result = encrypt_message_rsa(text, public_key)

        return render_template('/indice.html', result=result)
    else:
        return render_template('/indice.html')

def md5_hash(text):
    md5 = hashlib.md5()
    md5.update(text.encode())
    hashed_text = md5.hexdigest()
    return hashed_text

def sha1_hash(text):
    sha1 = hashlib.sha1()
    sha1.update(text.encode())
    hashed_text = sha1.hexdigest()
    return hashed_text

def sha256_hash(text):
    sha256 = hashlib.sha256()
    sha256.update(text.encode())
    hashed_text = sha256.hexdigest()
    return hashed_text

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_message_rsa(message, public_key):
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted_message

if __name__ == '__main__':
    app.run(debug=True)
