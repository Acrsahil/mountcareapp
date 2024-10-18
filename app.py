from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import  DateField

# Create Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#Create a form class
class NamerForm(FlaskForm):
    name = StringField("Whats Your Blame",validators=[DataRequired()])
    submit = SubmitField('Submit')
    date = DateField('What is the Date',format='%Y-%m-%d')

# Create a route decorator
@app.route('/')
def index():
    first_name = "Binod Khadka"
    stuff = "I love Arch Linux"
    favorite_pizza =["Pepperoni","Cheese","Mushrooms",'Onions',"Pineapple",20]
    return render_template('index.html',first_name=first_name,stuff=stuff,favorite_pizza=favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',user_name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500

#Create Name Page
@app.route('/name',methods=['GET','POST'])
def name():
    name = None
    date = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        date = form.date.data
        form.name.data = ''
        form.date.data = ''
    return render_template('name.html',
                           name=name,
                           date=date,
                           form=form
    )


if __name__ == "__main__":
    app.run(debug=True)

