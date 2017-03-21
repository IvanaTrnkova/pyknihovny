from flask import Flask, url_for, render_template
from jinja2 import Markup

#__name__ promenna nastavena pythonem na jmeno aktualniho modulu
# v prvni prvne return string, az pak url_for


app = Flask(__name__)

@app.route('/')
#routa - funkce přiřazená k webové adrese, říká, co se stane když se na ni ukáže
def hello():
	return url_for("hello_english",
					username="Ivana",
					count=3)


@app.route('/hello/')
@app.route('/hello/<username>/')
@app.route('/hello/<username>/<int:count>/')
def hello_english(username=None, count=1):
	
	return render_template("hello.html", name=username)

@app.template_filter("em")
def em(text):
	return Markup("<em>{}</em>").format(text)


