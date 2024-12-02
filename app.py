from flask import Flask, render_template, request, session
from functions import generate_captcha
from base64 import b64encode
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "ECRk19hdjM9u75vqcnT8OusWVCN69xsLYQ3ZRqETDeM="

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        captcha = request.form['captcha']
        if check_password_hash(session['captcha'], captcha):
            return 'success'
    captcha_bytes, random_text = generate_captcha()
    captcha_data = b64encode(captcha_bytes.getvalue()).decode('utf-8')
    session['captcha'] = generate_password_hash(random_text)
    return render_template('login.html', captcha_data=captcha_data, random_text=random_text)

if __name__ == '__main__':
    app.run()