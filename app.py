from random import randint

from flask import Flask, render_template, flash, redirect, url_for, session, request

from config import Config
from forms.StartForm import StartForm
from models.minefield import Minefield
from models.barman import Barman

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def main():
    form = StartForm()
    if form.validate_on_submit():
        session['username'] = form.username.data
        session['dif_mode'] = form.difficulty_level.data
        session['id_game'] = form.username.data + str(randint(1, 100))
        barman = Barman()
        barman.add_game(session['id_game'], session['dif_mode'])
        return redirect(url_for('minefield'))

    return render_template('main.html', form=form)


@app.route('/minefield', methods=['GET', 'POST'])
def minefield():
    barman = Barman()
    game = barman.take_game(session['id_game'])

    if request.method == 'POST':
        row, column = map(int, request.form['sub_btn'].split(':'))
        game.show()
        game.open_cell(row, column)

        if game.game_over:
            print('GAME OVER')
            if game.is_win:
                print('YOU WIN')
            else:
                print('YOU LOSE')

            game.open_all_cells()

    return render_template('minefield.html', obj=game)


if __name__ == '__main__':
    app.run(debug=True)
