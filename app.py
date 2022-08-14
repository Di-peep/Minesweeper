from flask import Flask, render_template, flash, redirect, url_for, session

from config import Config
from forms.StartForm import StartForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def main():
    form = StartForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        return redirect(url_for('minefield'))

    return render_template('main.html', form=form)


@app.route('/minefield', methods=['GET', 'POST'])
def minefield():
    return render_template('minefield.html', name=session['username'])


if __name__ == '__main__':
    app.run(debug=True)
