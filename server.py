from flask import Flask, request, jsonify
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
"""
               作者：zangcc
项目地址：https://github.com/zangcc
                                                                         
              Author: zangcc
Project address: https://github.com/zangcc                                                                                                                       
                                                                         
888888888  ,adPPYYba,  8b,dPPYba,    ,adPPYb,d8   ,adPPYba,   ,adPPYba,  
     a8P"  ""     `Y8  88P'   `"8a  a8"    `Y88  a8"     ""  a8"     ""  
  ,d8P'    ,adPPPPP88  88       88  8b       88  8b          8b          
,d8"       88,    ,88  88       88  "8a,   ,d88  "8a,   ,aa  "8a,   ,aa  
888888888  `"8bbdP"Y8  88       88   `"YbbdP"Y8   `"Ybbd8"'   `"Ybbd8"'  
                                     aa,    ,88                          
                                      "Y8bbdP"                           

"""
app = Flask(__name__)

secret_key = b'1234567890123456'  # 密钥必须是16个字节

def decrypt(encrypted_text):
    encrypted_data = base64.b64decode(encrypted_text)
    cipher = Cipher(algorithms.AES(secret_key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    return decrypted_data.decode('utf-8')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    encrypted_password = data.get('encryptedPassword')

    print(f"Received login request: username={username}, encrypted_password={encrypted_password}")

    decrypted_password = decrypt(encrypted_password)
    print(f"Decrypted password: {decrypted_password}")

    if username == 'admin' and decrypted_password.strip() == '123456':
        print("Login successful")
        return jsonify(message='Login Successful'), 200
    else:
        print("Login failed")
        return jsonify(message='Login Failed'), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5011)

