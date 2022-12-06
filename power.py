


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
from joblib import dump, load
import datetime as dt
app = Flask(__name__)

#filename = "models/model.pkl"
filename_arima = 'models/model_arima.pkl'
# filename_rnn = 'models/rnn_predictions.pkl'



with open(filename_arima, 'rb') as file:
    model_arima = load(file)

# with open(filename_rnn, 'rb') as file:
#     model_rnn = load(file)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    
    # Inputs
    year = int(request.form['year'])    
    month = int(request.form['month'])
    day = int(request.form['day'])

    date = pd.Timestamp(year=year,month=month,day=day)
    
    # Arima predictions
    forecast_arima = model_arima.predict(start=364, end=364 + 7, typ='levels').rename('ARIMA Forecast')
    output_arima = round(forecast_arima.loc[date],2)
    
    #RNN predictions
    df = pd.read_pickle('models/rnn_predictions.pkl')
    output_rnn = df.loc[date][0]

    return render_template('index.html', prediction_text=
                           #'Arima model prediction with mape 1.6 %  =  {} '.format( output_arima))
                           (f"Arima model prediction (mape= 1.56 %)  =   {output_arima}  and    RNN model prediction (mape= 2.04 %)  =  {output_rnn}"))
#                            (f"Arima model prediction with mape 1.6 %  =  {output_arima} "),
#                             prediction_text2=(f"{nl}RNN model prediction with mape 2.1 %  =  {output_rnn}"))


if __name__ == "__main__":
    app.run(debug=True)

