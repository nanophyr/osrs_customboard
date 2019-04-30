from flask import * 
import os
import scrape

app = Flask(__name__)

@app.route('/')
def home():
    flash(scrape.getTotal('nanoluck'))
    return render_template('home.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(debug=True)

