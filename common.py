from flask import * 
import os

app = Flask(__name__)

@app.route('/')
def home():
    flash('test')
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)

