from flask import Flask, url_for

#__name__ promenna nastavena pythonem na jmeno aktualniho modulu

app = Flask(__name__)

@app.route('/')
#routa - funkce přiřazená k webové adrese, říká, co se stane když se na ni ukáže
def hello():
    return url_for()


@app.route('/hello/')
@app.route('/hello/<username>/')
@app.route('/hello/<username>/<int:count>/')
def hello_english(username=None, count=1):
    return 'Hello {}! '.format(username) * count




