from flask import Flask, render_template, request, redirect
import numpy as np
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def select_cipher():
    if request.method == "GET":
        return render_template("/home1.html")
    else:
        cipher_choice = request.form["cipher_choice"]
        if cipher_choice == "vigenere":
            return redirect("/vigenere")
        elif cipher_choice == "vernam":
            return redirect("/vernam")
        elif cipher_choice == "shift":
            return redirect("/shift")
        elif cipher_choice == "playfair":
            return redirect("/playfair")
        elif cipher_choice == "hill":
            return redirect("/hill")
        else:
            return "Invalid cipher choice"
@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    if request.method == "GET":
        return render_template("vigenere.html")
    else:
        try:
            choice = int(request.form["choice"])
            key = request.form["key"].lower()

            if choice not in (1, 2):
                return render_template("Choose proper operations")

            if choice == 1:
                plain = request.form["plain"].lower()
                encrypt = []
                n = len(plain)
                j = 0
                for i in range(0, n):
                    if plain[i] == " ":
                        encrypt.append(plain[i])
                        continue
                    for k in range(0, len(mylist)):
                        if plain[i] == mylist[k]:
                            a1 = k
                    for k in range(0, len(mylist)):
                        if key[j % len(key)] == mylist[k]:
                            a2 = k
                    ans = a1 + a2
                    ans1 = ans % 26
                    encrypt.append(mylist[ans1])
                    j += 1
                return render_template("vigenere.html", encrypted_text=encrypt, choice=choice)

            elif choice == 2:  
                cipher = request.form["cipher"]
                cipher = cipher.lower()  
                decrypt = []
                j = 0
                for i in range(0, len(cipher)):
                    if cipher[i] == " ":
                        decrypt.append(cipher[i])
                        continue
                    for k in range(0, len(mylist)):
                        if cipher[i] == mylist[k]:
                            a1 = k
                    for k in range(0, len(mylist)):
                        if key[j % len(key)] == mylist[k]:
                            a2 = k
                    ans = a1 - a2
                    if ans < 0:
                        ans1 = ans + 26
                    else:
                        ans1 = ans % 26
                    decrypt.append(mylist[ans1])
                    j += 1
                return render_template("vigenere.html", decrypted_text=decrypt, choice=choice)

        except (ValueError, KeyError):
            return render_template("Invalid input or key format")
@app.route("/vernam", methods=["GET", "POST"])
def vernam():
    if request.method == "GET":
        return render_template("vernam.html")
    else:
        try:
            choice = int(request.form["choice"])
            key = request.form["key"].lower()

            if choice not in (1, 2):
                return render_template("Choose proper operations")
            if choice==1:
                plain=request.form["plain"]
                encrypt=[]
                for i in range(0,len(plain)):
                    if len(key)!=len(plain):
                        print(" ERROR !..length of key and plain should be same")
                        exit()
                    for k in range(0,len(mylist)):
                        if plain[i]==mylist[k]:
                            a1=k
                    for k in range(0,len(mylist)):
                        if key[i]==mylist[k] and i<=len(key):
                            a2=k
                    ans=a1^a2
                    ans1=ans%26
                    encrypt.append(mylist[ans1])
                return render_template("vernam.html",encrypted_text=encrypt,choice=choice)
            elif choice==2:
                cipher=request.form["cipher"]
                decrypt=[]
                for i in range(0,len(cipher)):
                    if len(key)!=len(cipher):
                        print("ERROR !...length of key and cipher should be same")
                        exit()
                    for k in range(0,len(mylist)):
                        if cipher[i]==mylist[k]:
                            a1=k
                    for k in range(0,len(mylist)):
                        if key[i]==mylist[k] and i<=len(key):
                            a2=k
                    ans=a1^a2
                    ans1=ans%26
                    decrypt.append(mylist[ans1])
                return render_template("vernam.html",decrypted_text=decrypt,choice=choice)
        except (ValueError, KeyError):
            return render_template("Invalid input or key format")
@app.route("/shift", methods=["GET", "POST"])
def shift():
    if request.method=="GET":
        return render_template('shift.html')
    else:
        mylist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        choice=int(request.form["choice"])
        if choice==1:
            name=request.form["name"].lower()
            key=int(request.form["key"])
            name=name.lower()
            cipher=[]
            for k in range(0,len(name)):
                for j in range(0,len(mylist)):
                    if name[k]==" ":
                        continue
                    if name[k]==mylist[j]:
                        ans=(j+key)%26
                        cipher.append(mylist[ans])
            return render_template("shift.html",cipher=cipher,choice=choice)
        elif choice==2:
            cipher_txt=request.form["cipher_text"]
            key=int(request.form["key"])
            plain=[]
            for k in range(0,len(cipher_txt)):
                for j in range(0,len(mylist)):
                    if cipher_txt[k]==mylist[j]:
                        if j>=key:
                           ans=(j-key)%26
                           plain.append(mylist[ans])
                        else:
                           ans=((j-key)+26)%26
                           plain.append(mylist[ans])
            return render_template("shift.html",plain=plain,choice=choice)
        else:
            return render_template("Choose proper operation")
@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    if request.method == "GET":
        return render_template("playfair.html")
    else:
        try:
            key=request.form["key"]
            mylist1=[]
            key1=[]
            key1.append(key[0])
            for i in range(1,len(key)):
                if key[i] not in key1:
                    key1.append(key[i])
            mylist1.extend(key1)
            for i in range(0,len(mylist)):
                if mylist[i] in key1:
                    continue
                else:
                    mylist1.append(mylist[i])
            m=len(mylist1)
            for i in range(0,m):
                if mylist1[i]=='i':
                    mylist1[i]='j'
                m=len(mylist1)
            mylist2=[]
            mylist2.append(mylist1[0])
            for i in range(0,len(mylist1)):
                if mylist1[i] not in mylist2:
                    mylist2.append(mylist1[i])
            a = 0
            matrix = []
            for i in range(5):
                row = []
                for j in range(5):
                    row.append(mylist2[a])
                    a += 1            
                matrix.append(row)
            choice=int(request.form["choice"])
            if choice==1:
                plain=request.form["plain"]
                plain1=[]
                for i in range(0,len(plain)):
                    if plain[i]==" ":
                        continue
                    if plain[i]=='i':
                        f='j'
                        plain1.append(f)
                    if plain[i]!='i':
                        plain1.append(plain[i])
                m=len(plain1)%2
                if m==1:
                    plain1.insert(len(mylist2),'x')
                n=len(plain1)/2
                cipher=[]
                for i in range(0,int(n)):
                    c1=[]
                    m=0
                    for j in range(0,2):
                        c1.append(plain1[j-m])
                        plain1.remove(plain1[j-m])
                        m+=1
                    for k in range(0,5):
                        for l in range(0,5):
                            if c1[0]==matrix[k][l]:
                                a1=k
                                a2=l
                            if c1[1]==matrix[k][l]:
                                a3=k
                                a4=l
                    if a1==a3:
                        a2=(a2+1)%5
                        a4=(a4+1)%5
                        cipher.append(matrix[a1][a2])
                        cipher.append(matrix[a3][a4])
                    elif a2==a4:
                        a1=(a1+1)%5
                        a3=(a3+1)%5
                        cipher.append(matrix[a1][a2])
                        cipher.append(matrix[a3][a4])
                    else:
                        a2,a4=a4,a2
                        cipher.append(matrix[a1][a2])
                        cipher.append(matrix[a3][a4])
                    c1.clear()
                return render_template("playfair.html",encrypted_text=cipher,choice=choice)
            elif choice == 2:
                cipher = request.form["cipher"]
                cipher1 = []
                for i in range(0, len(cipher)):
                    cipher1.append(cipher[i])
                n = len(cipher1) / 2
                p = []
                for i in range(0, int(n)):
                    p1 = []
                    m = 0
                    for j in range(0, 2):
                        p1.append(cipher1[j - m])
                        cipher1.remove(cipher1[j - m])
                        m += 1
                    for k in range(0, 5):
                        for l in range(0, 5):
                            if p1[0] == matrix[k][l]:
                                a1 = k
                                a2 =l
                            if p1[1] == matrix[k][l]:
                                a3 = k
                                a4 = l
                    if a1 == a3:
                        a2=(a2-1)%5
                        a4=(a4-1)%5    
                    elif a2 == a4:
                        a1=(a1-1)%5
                        a3=(a3-1)%5    
                    else:
                        a2, a4 = a4, a2
                    p.append(matrix[a1][a2])
                    p.append(matrix[a3][a4])
                    p1.clear()
                return render_template("playfair.html",decrypted_text=p,choice=choice)
            
           
        except (ValueError, KeyError):
            return render_template("Invalid input or key format")
@app.route("/ceasar", methods=["GET", "POST"])
def ceasar():
    if request.method == "GET":
        return render_template("ceasar.html")
    else:
        choice = int(request.form["choice"])
        name = request.form["name"].lower()
        cipher = []
        plain = []

        if choice == 1:
            for k in range(0, len(name)):
                for j in range(0, len(mylist)):
                    if name[k] == " ":
                        continue
                    if name[k] == mylist[j]:
                        ans = (j + 3) % 26
                        cipher.append(mylist[ans])
            return render_template("ceasar.html", cipher=cipher, choice=choice)

        elif choice == 2:
            for k in range(0, len(request.form["cipher_txt"])):
                for j in range(0, len(mylist)):
                    if request.form["cipher_txt"][k] == mylist[j]:
                        if j >= 3:
                            ans = (j - 3) % 26
                        else:
                            ans = ((j - 3) + 26) % 26
                        plain.append(mylist[ans])
            return render_template("ceasar.html", plain=plain, choice=choice)

        else:
            return render_template("ceasar.html", error="Choose correct option")


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = mod_inverse(det, modulus)  # Modular multiplicative inverse of the determinant
    if det_inv is None:
        raise ValueError("The matrix is not invertible under this modulus")
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    return matrix_mod_inv

def encrypt(plaintext, key_matrix):
    n = key_matrix.shape[0]
    plaintext = plaintext.lower().replace(" ", "")
    plaintext_vector = [ord(char) - ord('a') for char in plaintext]
    
    # Padding plaintext to make its length a multiple of the key size
    if len(plaintext_vector) % n != 0:
        for _ in range(n - len(plaintext_vector) % n):
            plaintext_vector.append(ord('x') - ord('a'))
    
    ciphertext_vector = []
    for i in range(0, len(plaintext_vector), n):
        chunk = plaintext_vector[i:i+n]
        chunk = np.dot(key_matrix, chunk) % 26
        ciphertext_vector.extend(chunk)
    
    ciphertext = ''.join(chr(int(num) + ord('a')) for num in ciphertext_vector)
    return ciphertext

def decrypt(ciphertext, key_matrix):
    n = key_matrix.shape[0]
    ciphertext_vector = [ord(char) - ord('a') for char in ciphertext]
    
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)
    
    plaintext_vector = []
    for i in range(0, len(ciphertext_vector), n):
        chunk = ciphertext_vector[i:i+n]
        chunk = np.dot(key_matrix_inv, chunk) % 26
        plaintext_vector.extend(chunk)
    
    plaintext = ''.join(chr(int(num) + ord('a')) for num in plaintext_vector)
    return plaintext

@app.route('/', methods=['GET', 'POST'])
def index():
    ciphertext = None
    plaintext = None
    error = None
    
    if request.method == 'POST':
        choice = request.form['choice']
        matrix_size = int(request.form['matrix_size'])
        key_matrix = []

        # Construct the key matrix
        for i in range(matrix_size):
            row_input = request.form[f'row_{i+1}'].split()
            if len(row_input) != matrix_size:
                error = "Error: Each row of the key matrix must have the same number of elements."
                break
            row = list(map(int, row_input))
            key_matrix.append(row)
        
        if not error:
            key_matrix = np.array(key_matrix)

            if choice == 'encrypt':
                plaintext = request.form['plaintext']
                ciphertext = encrypt(plaintext, key_matrix)
            elif choice == 'decrypt':
                ciphertext = request.form['ciphertext']
                plaintext = decrypt(ciphertext, key_matrix)

    return render_template('index.html', ciphertext=ciphertext, plaintext=plaintext, error=error)

if __name__ == '__main__':
    app.run(debug=True)
