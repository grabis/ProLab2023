from models import PredictionModel
from scipy.stats import *


def predict_quantity(predictionModel):
    optimalAmount = 0

    sp = predictionModel.selling_price
    pc = predictionModel.purchase_cost
    sc = predictionModel.scrap_value
    d = predictionModel.average_demand
    v = predictionModel.variability

    Cu = sp - pc
    Co = pc - sc

    CR = Cu/ (Cu+Co)

    optimalAmount=norm.ppf(CR,loc=d, scale=v)
    return optimalAmount

