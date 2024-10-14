from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

#Create a form class

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



if __name__ == "__main__":
    app.run(debug=True)
