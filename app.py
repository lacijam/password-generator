import random
import string

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    password_length = 8
    include_numbers = False
    include_symbols = False

    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        include_numbers = request.form.get('include_numbers')
        include_symbols = request.form.get('include_symbols')

        password = generate_password(password_length, include_numbers, include_symbols)

    return render_template('index.html', password=password, password_length=password_length, include_numbers=include_numbers, include_symbols=include_symbols)

if __name__ == '__main__':
    app.run()

def generate_password(password_length, include_numbers, include_symbols):
    password = ""
    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    for i in range(password_length):
        password += random.choice(characters)

    return password

