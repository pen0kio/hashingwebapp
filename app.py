import hashlib
import os
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET"])
def mainpage():
    return render_template('mainpage.html')

@app.route('/decrypt', methods=["POST", "GET"])
def decrypt():
    if request.method == "GET":
        valuee = "If cracked plain text will appear here"
        return render_template('decrypt.html', valuee = valuee)
    elif request.method == "POST":
        hash = str(request.form['hash'])
        type = str(request.form['type'])
        valuee = "Sorry! Unable to decrypt the hash."
        wordList = str(os.path.join(os.getcwd(), 'static', 'rockyou.txt'))
        if type == "md5":
            passwords = open(wordList, 'r')
            for word in passwords:
                encodeWord = word.encode('UTF-8')
                md5Hash = hashlib.md5(encodeWord.strip()).hexdigest()    
                if md5Hash == hash:
                    valuee = word
                    break
            passwords.close()
        elif type == "sha1":            
            passwords = open(wordList, 'r')
            for word in passwords:
                encodeWord = word.encode('UTF-8')
                sha1Hash = hashlib.sha1(encodeWord.strip()).hexdigest()    
                if sha1Hash == hash:
                    valuee = word
                    break
            passwords.close()
        elif type == "sha224":            
            passwords = open(wordList, 'r')
            for word in passwords:
                encodeWord = word.encode('UTF-8')
                sha244Hash = hashlib.sha224(encodeWord.strip()).hexdigest()    
                if sha244Hash == hash:
                    valuee = word
                    break
            passwords.close()
        elif type == "sha256":            
            passwords = open(wordList, 'r')
            for word in passwords:
                encodeWord = word.encode('UTF-8')
                sha256Hash = hashlib.sha256(encodeWord.strip()).hexdigest()    
                if sha256Hash == hash:
                    valuee = word
                    break
            passwords.close()
        elif type == "sha512":            
            passwords = open(wordList, 'r')
            for word in passwords:
                encodeWord = word.encode('UTF-8')
                sha512Hash = hashlib.sha512(encodeWord.strip()).hexdigest()    
                if sha512Hash == hash:
                    valuee = word
                    break
            passwords.close()
        return render_template('decrypt.html', valuee = valuee)

@app.route('/encrypt', methods=["POST", "GET"])
def encrypt():
    vals = {"md5": "md5 Hash will appear here", "sha1": "sha1 Hash will appear here", "sha224": "sha224 Hash will appear here", "sha256": "sha256 Hash will appear here", "sha512": "sha512 Hash will appear here"}
    if request.method == "POST":
        hashValue = str(request.form['plain'])
        hashmd5 = hashlib.md5()
        hashmd5.update(hashValue.encode())
        vals['md5'] = str(hashmd5.hexdigest())
        hashsha1 = hashlib.sha1()
        hashsha1.update(hashValue.encode())
        vals['sha1'] = str(hashsha1.hexdigest())
        hashsha224 = hashlib.sha224()
        hashsha224.update(hashValue.encode())
        vals['sha224'] = str(hashsha224.hexdigest())
        print('SHA224 Hash: ' + hashsha224.hexdigest())
        hashsha256 = hashlib.sha256()
        hashsha256.update(hashValue.encode())
        vals['sha256'] = str(hashsha256.hexdigest())
        hashsha512 = hashlib.sha512()
        hashsha512.update(hashValue.encode())
        vals['sha512'] = str(hashsha512.hexdigest())     
        return render_template('encrypt.html', vals = vals)
    return render_template('encrypt.html', vals =vals)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='80')