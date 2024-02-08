from flask import Flask, render_template, redirect, url_for, request, flash
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_login import login_user, LoginManager, current_user, logout_user, UserMixin
from forms import AdminForm, AddCafeForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["SECRET_KEY"] = "33erdbkdzsriugiut48mdbvdiy"
Base = declarative_base()
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db.init_app(app)
Bootstrap5(app)

login_manager = LoginManager()
login_manager.init_app(app)
CAME_FROM_ADD = False


@login_manager.user_loader
def load_user(admin_id):
    return db.get_or_404(Admin, admin_id)


class Cafes(db.Model):
    __tablename__ = "cafe"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    map_url = Column(String, nullable=False)
    img_url = Column(String, nullable=False)
    location = Column(String, nullable=False)
    has_sockets = Column(Integer, nullable=False)
    has_toilet = Column(Integer, nullable=False)
    has_wifi = Column(Integer, nullable=False)
    can_take_calls = Column(Integer, nullable=False)
    seats = Column(String, nullable=False)
    coffee_price = Column(String, nullable=False)


class Admin(UserMixin, db.Model):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    cafes = db.session.execute(db.select(Cafes)).scalars().all()
    return render_template("index.html", cafes=cafes)


@app.route("/cafe/<int:cafe_id>", methods=["GET", "POST"])
def show_cafe(cafe_id):
    cafe = db.get_or_404(Cafes, cafe_id)
    return render_template("cafe.html", cafe=cafe, current_user=current_user)


# # -------------------------- Use this to add admins -------------------------------
# @app.route("/register", methods=["GET", "POST"])
# def register():
#     form = AdminForm()
#     if form.validate_on_submit():
#         result = db.session.execute(
#             db.select(Admin).where(Admin.username == form.username.data)
#         )
#         admin = result.scalar()
#         hashed_pass = generate_password_hash(form.password.data, salt_length=8)
#         new_admin = Admin(username=form.username.data, password=hashed_pass)
#         db.session.add(new_admin)
#         db.session.commit()
#     return render_template("admin.html", form=form)


# ----------------------------------------------------------------------------------


@app.route("/login", methods=["GET", "POST"])
def login():
    admin_form = AdminForm()
    if admin_form.validate_on_submit():
        username = admin_form.username.data
        password = admin_form.password.data
        result = db.session.execute(db.select(Admin).where(Admin.username == username))
        admin = result.scalar()
        if not admin:
            flash("Wrong username or password")
            return redirect(url_for("login"))
        if not check_password_hash(admin.password, password):
            flash("Wrong username or password")
            return redirect(url_for("login"))
        else:
            login_user(admin)
            global CAME_FROM_ADD
            if CAME_FROM_ADD:
                CAME_FROM_ADD = False
                return redirect(url_for("add_cafe"))
            else:
                return redirect(url_for("home"))
    return render_template("admin.html", form=admin_form)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    if not current_user.is_authenticated:
        global CAME_FROM_ADD
        CAME_FROM_ADD = True
        return redirect(url_for("login"))
    add_cafe_form = AddCafeForm()
    if add_cafe_form.validate_on_submit():
        new_cafe = Cafes(
            name=add_cafe_form.name.data,
            map_url=add_cafe_form.map_url.data,
            img_url=add_cafe_form.img_url.data,
            location=add_cafe_form.location.data,
            has_sockets=add_cafe_form.has_sockets.data,
            has_toilet=add_cafe_form.has_toilet.data,
            has_wifi=add_cafe_form.has_wifi.data,
            can_take_calls=add_cafe_form.can_take_calls.data,
            seats=add_cafe_form.seats.data,
            coffee_price=add_cafe_form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template(
        "add-post.html",
        form=add_cafe_form,
    )


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/delete/<int:id>")
def delete_cafe(id):
    cafe = db.get_or_404(Cafes, id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
