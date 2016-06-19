from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    return redirect(url_for('index'))


app.run(debug=True)