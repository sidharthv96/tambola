# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt
from dataclasses import dataclass

from flask_login import UserMixin

from tambola.database import (
    Column,
    Model,
    SurrogatePK,
    db,
    reference_col,
    relationship,
)
from tambola.extensions import bcrypt


@dataclass
class Game(SurrogatePK, Model):
    numbers: str
    __tablename__ = "game"

    numbers = Column(db.String(300), default="", nullable=False)
    tickets = relationship("Ticket")

@dataclass
class Ticket(SurrogatePK, Model):
    name: str
    game: int
    data: str
    """A ticket for a game."""

    __tablename__ = "ticket"
    name = Column(db.String(80), unique=True, nullable=False)
    game = Column(db.Integer, db.ForeignKey('game.id'))
    data = Column(db.String(300), nullable=False)
    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Ticket({self.name},game={self.game})>"

