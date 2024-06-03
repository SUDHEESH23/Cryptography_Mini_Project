from flask import Flask, render_template, request

app = Flask(__name__)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/ceasar", methods=["GET", "POST"])
def ceasar():
    if request.method == "GET":
        return render_template("ceasar.html")
    else:
        choice = int(request.form.get("choice", 0))  # Get choice from form, default to 0 if not found
        name = request.form.get("name", "").lower()  # Get name from form, default to empty string if not found
        cipher_txt = request.form.get("cipher_txt", "").lower()
        cipher = []
        plain = []

        if choice == 1:
            for char in name:
                if char == " ":
                    continue
                ans = (mylist.index(char) + 3) % 26
                cipher.append(mylist[ans])
            return render_template("ceasar.html", cipher=cipher, choice=choice)

        elif choice == 2:
            for char in cipher_txt:
                if char == " ":
                    continue
                ans = (mylist.index(char) + 3) % 26  # Adding the key (3) instead of subtracting
                plain.append(mylist[ans])
            return render_template("ceasar.html", plain=plain, choice=choice)



        else:
            return render_template("ceasar.html", error="Please choose a correct option")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
