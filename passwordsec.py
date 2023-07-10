import re
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        if is_secure_password(password):
            return "Password is secure!"
        else:
            return "Password is not secure. Please enter a secure password."
    return render_template('index.html')


def is_secure_password(password):
    # Check the password for security criteria
    if len(password) < 8:
        return False

    if not re.search(r'[A-Z]', password):
        return False

    if not re.search(r'[a-z]', password):
        return False

    if not re.search(r'\d', password):
        return False

    if not re.search(r'[^A-Za-z0-9]', password):
        return False

    return True


if __name__ == '__main__':
    app.run(debug=True)