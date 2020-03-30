from flask import Flask, render_template
from data import db_session, __all_models
from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired

User = __all_models.users.User
Jobs = __all_models.jobs.Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Войти')


def main():
    db_session.global_init("db/Mars.sqlite")
    session = db_session.create_session()
    user_1 = User()
    user_1.surname = "Scheblykin"
    user_1.name = "Sergey"
    user_1.age = 16
    user_1.position = "mayor"
    user_1.speciality = "nurse"
    user_1.address = "module_2"
    user_1.email = "CrusadOr@mars.org"

    user_2 = User()
    user_2.surname = "Snegov"
    user_2.name = "Konstantin"
    user_2.age = 16
    user_2.position = "lieutenant"
    user_2.speciality = "programmer"
    user_2.address = "module_3"
    user_2.email = "snowbones@mars.org"

    user_3 = User()
    user_3.surname = "Morozov"
    user_3.name = "Vyacheslav"
    user_3.age = 15
    user_3.position = "mayor"
    user_3.speciality = "research engineer's secretary"
    user_3.address = "module_4"
    user_3.email = "top4eg@mars.org"

    captain = User()
    captain.surname = "Scott"
    captain.name = "Ridley"
    captain.age = 21
    captain.position = "captain"
    captain.speciality = "research engineer"
    captain.address = "module_1"
    captain.email = "scott_chief@mars.org"

    session.add(captain)
    session.add(user_1)
    session.add(user_2)
    session.add(user_3)

    session.commit()
    app.run()


@app.route("/")
def index():
    session = db_session.create_session()
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        session = db_session.create_session()
        if session.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        session.add(user)
        session.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
