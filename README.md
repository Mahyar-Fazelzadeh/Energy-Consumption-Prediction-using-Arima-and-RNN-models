# Power consumption of Tetouan city
## Introduction

We are all aware of dangerous of over consuming energy in future. Right now lots of countries are suffering to provide enough energy for their daily consumptions. Any tools to be able to predict the pattern of energy consuption will help countries to plan for their future.
In this project two models are developed to forcast the energy consumption of a city.

![bird](https://github.com/Mahyar-Fazelzadeh/convolutional_neural_network_bird_classification/blob/main/assets/Birds1.JPG)

## Dataset
Dataset is obtaned from 
https://archive.ics.uci.edu/ml/datasets/Power+consumption+of+Tetouan+city

It is energy consumption of Tetouan city in north of africa. There are 3 differnt zones(3 different part of the city). Zone 1 and 2 are residental with larger consumption average, zone 3 is a beach area including hotels and spas.

Originla data has 10 minutes interval. For this project, data is converted to have a daily interval.

For this project I focused on Zone 1. I developed two models to be trained for the period of January 2017 to December 2018 to be able to predict the energy consumption of the first week of 2018.

## Models:
### Arima Model:
Since the data has a sesonal pattern with seasonal period of 7 days, I used Sarima with order= (3,0,4) and seasonal order=(1,1,1)[7].

Here is the prediction for 2018:

![bird](https://github.com/Mahyar-Fazelzadeh/convolutional_neural_network_bird_classification/blob/main/assets/Birds1.JPG)

### RNN Model:
#### Details of the model:
- 6 LSTM layers with a range of [170, 120] neurons
- all activation functions are relu
- Dropout with the rate = 0.1
- Optimizer = adam loss_function = mse
- epochs = 220

You can find the best RNN model here:
###################

Here is the prediction for 2018:
![bird](https://github.com/Mahyar-Fazelzadeh/convolutional_neural_network_bird_classification/blob/main/assets/Birds1.JPG)

## Cross Validation
5 fold cross validation with test size equal to 7 days
![bird](https://github.com/Mahyar-Fazelzadeh/convolutional_neural_network_bird_classification/blob/main/assets/Birds1.JPG)

here is the tables of metrics of each fold for arima model:
![bird](https://github.com/Mahyar-Fazelzadeh/convolutional_neural_network_bird_classification/blob/main/assets/Birds1.JPG)
here is the tables of metrics of each fold for arima model:
![bird](https://github.com/Mahyar-Fazelzadeh/convolutional_neural_network_bird_classification/blob/main/assets/Birds1.JPG)

There are variations in all metrics among different folds, But this level of variation is normal and within acceptable range. Therefore, both models are accepted. 

## Comparing two models:
At this level, Arima model performed better based on the rmse and mape metrics. But it does not mean that the RNN model has not the potensial to get a better result. Playing with Nueral network parameters to gain best result is time consuming process. It is recomended to test other parameters in RNN model to get a better result.












Here is the Gantt chart including the tasks and expected timeline:

![timeline](https://github.com/Mahyar-Fazelzadeh/Tetuan_City_power_consumption_analysis/blob/main/timeline_pic.png)

