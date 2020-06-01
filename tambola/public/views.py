# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    json
)
from flask_login import login_required, login_user, logout_user

from tambola.extensions import login_manager
from tambola.public.forms import LoginForm
from tambola.public.util import Generator, get_name
from tambola.user.forms import RegisterForm
from tambola.user.models import User, Ticket, Config
from tambola.utils import flash_errors
import random

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    current_app.logger.info("Hello from the home page!")
    # Handle logging in
    if request.method == "POST":
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
    return render_template("public/home.html", form=form)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/tickets/")
@login_required
def tickets():
    return json.jsonify(Ticket.query.filter_by(game=request.args.get('game', '1')).all())
    

@blueprint.route("/play/")
def play():
    """Play page."""
    
    return render_template("public/play.html", card=Ticket.create(
        name=get_name(),
        game=get_game().value,
        data=json.dumps(Generator().get_ticket())
    ))


@blueprint.route("/game/")
def game():
    """set game."""
    game = get_game()
    return game.value


@blueprint.route("/game/new")
@login_required
def game_inc():
    """new game."""
    game = get_game()
    game.value = str(int(game.value) + 1)
    game.save()
    return game.value


def get_game():
    game = Config.get_by_name(name="game.name")
    if not game:
        game = Config.create(
            name="game.name",
            value="1"
        )
    return game
