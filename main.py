from flask import Flask, render_template

app = Flask(__name__)

# 1. Bosh sahifa (Hero va About qismlari bilan)
@app.route('/')
def home():
    return render_template('index.html')

# 2. Loyihalar sahifasi (Sizning 3 ta asosiy loyihangiz uchun)
@app.route('/projects')
def projects():
    return render_template('projects.html')

# 3. Aloqa sahifasi (Agar alohida sahifa qilsangiz, hozircha indexga qaytaradi)
@app.route('/contact')
def contact():
    return render_template('index.html', _anchor='contact')

if __name__ == '__main__':
    # debug=True xatoliklarni aniqlashga yordam beradi
    app.run(debug=True host=127.0.0.1)

