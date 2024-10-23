from flask import Flask, request, render_template
from models import PredictionModel
from flask_sqlalchemy import SQLAlchemy
import prediction

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Apps\\cake2024_demo.db'

db = SQLAlchemy(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'
@app.route('/predictionModels', methods=['GET'])
def getPredictionModels():
    predictionsAll = db.session.query(PredictionModel).all()

    return render_template("predictions2.html", predictions=predictionsAll)

@app.route('/predictionModels/<mid>', methods=['GET'])
def getPredictionModel(mid=1):
    prediction = db.session.query(PredictionModel).filter(PredictionModel.id==mid).all()

    return str(len(prediction))

@app.route('/predict', methods=['GET'])
def predict():
    d = int (request.args.get('d'))
    v = int(request.args.get('v'))
    pc = int(request.args.get('pc'))
    sp = int (request.args.get('sp'))
    sv = int (request.args.get('sv'))

    predictionModel = PredictionModel(average_demand=d,variability=v, purchase_cost=pc, selling_price=sp, scrap_value= sv,optimal_qty=0)

    predicted_quantity= prediction.predict_quantity(predictionModel)
    predictionModel.optimal_qty = 100
    #int(predicted_quantity)
    print(predicted_quantity)

    db.session.add(predictionModel)

    db.session.commit()

    return render_template("prediction.html", prediction=str(predicted_quantity))


if __name__ == '__main__':
    app.run()
