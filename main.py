from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

# I build this without using DB

app = Flask(__name__)
app.config['SECRET_KEY'] = "yuvi"
Bootstrap5(app)

to_do_list = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form
        to_do = data['todo']
        to_do_list.append(to_do)
        print(to_do)
        print(to_do_list)
        return render_template('index.html', to_dos=to_do_list)

    return render_template('index.html', to_dos=to_do_list)



@app.route("/del/<int:ind>")
def remov(ind):
    to_delete = to_do_list[ind]
    to_do_list.remove(to_delete)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
