# Power consumption of Tetouan city
## Introduction

We are all aware of dangerous of over consuming energy in future. Right now lots of countries are suffering to provide enough energy for their daily consumptions. Any tools to be able to predict the pattern of energy consuption will help countries to plan for their future.
In this project two models are developed to forcast the energy consumption of a city.
<p align="center">
 <img width="600" src="https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/assets/Tetuan_city_zones.png" alt="Tetuan_city_zones">
</p>

## Dataset
Dataset is obtaned from 
https://archive.ics.uci.edu/ml/datasets/Power+consumption+of+Tetouan+city

It is energy consumption of Tetouan city in north of africa. There are 3 differnt zones(3 different part of the city). Zone 1 and 2 are residental with larger consumption average, zone 3 is a beach area including hotels and spas.

Originla data has 10 minutes interval. For this project, data is converted to have a daily interval.

For this project I focused on Zone 1. I developed two models to be trained for the period of January 2017 to December 2018 to be able to predict the energy consumption of the first week of 2018.

## Models:
### Arima Model:
Since the data has a sesonal pattern with seasonal period of 7 days, I used Sarima with order= (3,0,4) and seasonal order=(1,1,1)[7].

Here is the forecast for 2018:
<p align="center">
 <img width="900" src="https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/assets/Arima_future_prediction_plot.JPG" alt="Arima_future_prediction_plot">
</p>


### RNN Model:
#### Details of the model:
- 6 LSTM layers with a range of [170, 120] neurons
- all activation functions are relu
- Dropout with the rate = 0.1
- Optimizer = adam loss_function = mse
- epochs = 220

You can find the best RNN model here:
[model_rnn_relu_rmse66](https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/models/model_rnn_relu_rmse66.h5)

Here is the forecast for 2018:
<p align="center">
 <img width="900" src="https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/assets/RNN_future_forecast_plot.JPG" alt="RNN_future_forecast_plot">
</p>


## Cross Validation
5 fold cross validation with test size equal to 7 days
<p align="center">
 <img width="300" src="https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/assets/time_series_cv_plot.JPG" alt="time_series_cv_plot">
</p>


here is the tables of metrics of each fold, Arima model:
<p align="center">
 <img width="500" src="https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/assets/cv_arima_metrics.JPG" alt="cv_arima_metrics">
</p>

here is the tables of metrics of each fold, RNN model:
<p align="center">
 <img width="500" src="https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/assets/cv_rnn_metrics.JPG" alt="cv_rnn_metrics">
</p>


There are variations in all metrics among different folds, But this level of variation is normal and within acceptable range. Therefore, both models are accepted. 

## Comparing two models:
At this level, Arima model performed better based on the rmse and mape metrics. But it does not mean that the RNN model has not the potensial to get a better result. Playing with Nueral network parameters to gain best result is time consuming process. It is recomended to test other parameters in RNN model to get a better result.

## Deployment
You can run [power.py](https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/power.py) to visit the interface of future forecast of Tetaun city enrgy consumption.
