# -*- coding: utf-8 -*-
"""User views."""
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
from flask_login import login_required
from tambola.public.util import Generator, get_name
from tambola.game.models import Ticket, Game
from tambola.utils import flash_errors
import random
blueprint = Blueprint("game", __name__, url_prefix="/games", static_folder="../static")


@blueprint.route("/")
def game():
    return json.jsonify(get_game())

def get_rand():
    return str(random.randint(1, 90))

@blueprint.route("/random/")
@login_required
def game_random_number():
    game = get_game()
    numbers = game.numbers.split(",")
    rand = get_rand()
    while rand in numbers and len(numbers) <= 90:
        rand = get_rand()
    if numbers[0] == "":
        numbers[0] = rand
    else:
        numbers.append(str(rand))
    game.numbers = ",".join(numbers)
    game.save()
    return rand


@blueprint.route("/numbers/")
@login_required
def game_all_numbers():
    game = get_game()
    return game.numbers


@blueprint.route("/new/")
@login_required
def game_inc():
    """new game."""
    Game.create()
    return game()


def get_game():
    game = Game.query.order_by(Game.id.desc()).first()
    if not game:
        game = Game.create()
    return game


@blueprint.route("/tickets/")
@login_required
def tickets():
    game = get_game()
    return json.jsonify(game.tickets)
    

@blueprint.route("/play/")
def play():
    """Play page."""
    
    return render_template("public/play.html", card=Ticket.create(
        name=get_name(),
        game=get_game().id,
        data=json.dumps(Generator().get_ticket())
    ))