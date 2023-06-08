from flask_script import Command
from game import db
from game.models.mst_ranking import Ranking
from game.models.mst_answer import Answer

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()