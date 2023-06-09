from flask_script import Command
from pokemon import db
from pokemon.models.player_status import PlayerStatus
from pokemon.models.monster import Monster

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()