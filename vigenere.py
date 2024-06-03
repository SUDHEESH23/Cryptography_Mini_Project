from flask import Flask, render_template, request

app = Flask(__name__)

mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route("/vigenere", methods=["GET", "POST"])
def vigenere():
    if request.method == "GET":
        return render_template("vigenere.html")
    else:
        try:
            choice = int(request.form["choice"])
            key = request.form["key"].lower()

            if choice not in (1, 2):
                return render_template("vigenere.html", message="Choose a proper operation")

            if not key:
                return render_template("vigenere.html", message="Key cannot be empty")

            if not all(char.isalpha() for char in key):
                return render_template("vigenere.html", message="Key should contain only alphabetic characters")

            if choice == 1:
                plain = request.form["plain"].lower()
                encrypt = ""
                key_index = 0
                for char in plain:
                    if char.isalpha():
                        plain_index = mylist.index(char)
                        key_char = key[key_index % len(key)]
                        key_index += 1
                        key_index %= len(key)
                        key_shift = mylist.index(key_char)
                        encrypt += mylist[(plain_index + key_shift) % 26]
                    else:
                        encrypt += char
                return render_template("vigenere.html", encrypted_text=encrypt, choice=choice)

            elif choice == 2:
                cipher = request.form["cipher"].lower()
                decrypt = ""
                key_index = 0
                for char in cipher:
                    if char.isalpha():
                        cipher_index = mylist.index(char)
                        key_char = key[key_index % len(key)]
                        key_index += 1
                        key_index %= len(key)
                        key_shift = mylist.index(key_char)
                        decrypt += mylist[(cipher_index - key_shift) % 26]
                    else:
                        decrypt += char
                return render_template("vigenere.html", decrypted_text=decrypt, choice=choice)

        except (ValueError, KeyError):
            return render_template("vigenere.html", message="Invalid input or key format")

if __name__ == "__main__":
    app.run(debug=True, port=5500)
