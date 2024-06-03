from flask import Flask, render_template, request

app = Flask(__name__)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/playfair", methods=["GET", "POST"])
def playfair():
    if request.method == "GET":
        return render_template("playfair.html")
    else:
        try:
            key = request.form["key"]
            mylist1 = []
            key1 = []
            key1.append(key[0])
            for i in range(1, len(key)):
                if key[i] not in key1:
                    key1.append(key[i])
            mylist1.extend(key1)
            for i in range(0, len(mylist)):
                if mylist[i] in key1:
                    continue
                else:
                    mylist1.append(mylist[i])
            m = len(mylist1)
            for i in range(0, m):
                if mylist1[i] == 'i':
                    mylist1[i] = 'j'
            mylist2 = []
            mylist2.append(mylist1[0])
            for i in range(0, len(mylist1)):
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
            choice = int(request.form["choice"])
            if choice == 1:
                plain = request.form["plain"]
                plain1 = []
                for i in range(0, len(plain)):
                    if plain[i] == " ":
                        continue
                    if plain[i] == 'i':
                        f = 'j'
                        plain1.append(f)
                    if plain[i] != 'i':
                        plain1.append(plain[i])
                m = len(plain1) % 2
                if m == 1:
                    plain1.insert(len(mylist2), 'x')
                n = len(plain1) / 2
                cipher = []
                for i in range(0, int(n)):
                    c1 = []
                    m = 0
                    for j in range(0, 2):
                        c1.append(plain1[j - m])
                        plain1.remove(plain1[j - m])
                        m += 1
                    for k in range(0, 5):
                        for l in range(0, 5):
                            if c1[0] == matrix[k][l]:
                                a1 = k
                                a2 = l
                            if c1[1] == matrix[k][l]:
                                a3 = k
                                a4 = l
                    if a1 == a3:
                        a2 = (a2 + 1) % 5
                        a4 = (a4 + 1) % 5
                        cipher.append(matrix[a1][a2])
                        cipher.append(matrix[a3][a4])
                    elif a2 == a4:
                        a1 = (a1 + 1) % 5
                        a3 = (a3 + 1) % 5
                        cipher.append(matrix[a1][a2])
                        cipher.append(matrix[a3][a4])
                    else:
                        a2, a4 = a4, a2
                        cipher.append(matrix[a1][a2])
                        cipher.append(matrix[a3][a4])
                    c1.clear()
                return render_template("playfair.html", encrypted_text=cipher, choice=choice)
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
                                a2 = l
                            if p1[1] == matrix[k][l]:
                                a3 = k
                                a4 = l
                    if a1 == a3:
                        a2 = (a2 - 1) % 5
                        a4 = (a4 - 1) % 5
                    elif a2 == a4:
                        a1 = (a1 - 1) % 5
                        a3 = (a3 - 1) % 5
                    else:
                        a2, a4 = a4, a2
                    p.append(matrix[a1][a2])
                    p.append(matrix[a3][a4])
                    p1.clear()
                return render_template("playfair.html", decrypted_text=p, choice=choice)
            else:
                return render_template("playfair.html", error="Please choose a correct option")

        except (ValueError, KeyError):
            return render_template("playfair.html", error="Invalid input or key format")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
