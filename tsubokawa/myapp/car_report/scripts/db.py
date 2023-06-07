from flask_script import Command
from car_report import db
from car_report.models.reports import Report
from car_report.models.reports_mst import Mst_Report

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()