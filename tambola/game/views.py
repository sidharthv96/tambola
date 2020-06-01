# -*- coding: utf-8 -*-
"""User views."""
from flask import (
    Blueprint,
    render_template,
    make_response,
    request,
    json
)
from flask_login import login_required
from tambola.public.util import Generator, get_name
from tambola.game.models import Ticket, Game
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

    ticket_name = request.cookies.get('ticket_name')
    ticket = None
    game = get_game()
    new_ticket = True

    if ticket_name:
        ticket = Ticket.get_by_name(ticket_name)
        new_ticket = ticket and ticket.game != game.id
    if new_ticket:
        ticket = Ticket.create(
            name=get_name(),
            game=game.id,
            data=json.dumps(Generator().get_ticket())
        )
    resp = make_response(render_template("public/play.html", card=ticket, data=json.loads(ticket.data)))
    resp.set_cookie('ticket_name', ticket.name)
    return resp
