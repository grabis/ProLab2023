from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class PredictionModel(db.Model):

    __tablename__ = 'PredictionModel'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    average_demand = db.Column(db.Integer, nullable=False)
    variability = db.Column(db.Integer, nullable=False)
    purchase_cost = db.Column(db.Integer, nullable=False)
    selling_price = db.Column(db.Integer, nullable=False)
    scrap_value = db.Column(db.Integer, nullable=False)
    optimal_qty = db.Column(db.Integer, nullable=False)



    def __init__(self, average_demand, variability, purchase_cost, selling_price, scrap_value,optimal_qty):

        self.average_demand = average_demand
        self.variability = variability
        self.purchase_cost = purchase_cost
        self.selling_price = selling_price
        self.scrap_value = scrap_value
        self.optimal_qty=optimal_qty

class Cake():
    name = ''
