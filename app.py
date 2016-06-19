import json

from flask import (Flask,
                   render_template,
                   redirect,
                   url_for,
                   request,
                   make_response,
                   flash)

from options import DEFAULTS

app = Flask(__name__)
app.secret_key = 'rh5UXm{VK-eD8x+Ndp6+r?x,+iir=%|gm^SKP/vE@H 551A2p;0&qS#.#d9A~=E+'

def get_saved_data():
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    return render_template('index.html', saves=get_saved_data())


@app.route('/builder')
def builder():
    return render_template(
        'builder.html',
        saves=get_saved_data(),
        options=DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():
    flash('Your Bear is Saved!')
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response


app.run(debug=True)
