from flask_script import Command
from car_report import db
from car_report.models.reports import Report

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()