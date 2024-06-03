from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/shift", methods=["GET", "POST"])
def shift():
    if request.method == "GET":
        return render_template('shift.html')
    else:
        mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        try:
            choice = int(request.form["choice"])

            if choice == 1:
                name = request.form["name"].lower()
                key = int(request.form["key"])
                cipher = []

                for char in name:
                    if char == " ":
                        continue
                    for j in range(len(mylist)):
                        if char == mylist[j]:
                            ans = (j + key) % 26
                            cipher.append(mylist[ans])

                return render_template("shift.html", cipher=cipher, choice=choice)

            elif choice == 2:
                cipher_txt = request.form["cipher_text"]
                key = int(request.form["key"])
                plain = []

                for char in cipher_txt:
                    for j in range(len(mylist)):
                        if char == mylist[j]:
                            if j >= key:
                                ans = (j - key) % 26
                                plain.append(mylist[ans])
                            else:
                                ans = ((j - key) + 26) % 26
                                plain.append(mylist[ans])

                return render_template("shift.html", plain=plain, choice=choice)

            else:
                return render_template("shift.html", error="Choose proper operation")

        except ValueError:
            return render_template("shift.html", error="Invalid input for key or text")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
