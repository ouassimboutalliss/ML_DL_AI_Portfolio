# Red Wine Quality 



## Summary


## Project approach:

1) Problem understanding
2) Load data
3) Data exploring (check on inconsistent data, ...
4) Clean data (outliers, missing data, ...)
5) Analyse/visualize cleaned data (corr, describe dataset, ...)
6) Data preprocessing (split training/test, normalize, pca, feature engineering, ...)
7) Choosing model (based on problem/target (supervised, unsupervised)
8) Train model
9) Hyperparameter tuning (grid search, ...)
10) Evaluating model
11) Prediction
12) Save model (pickle)
13) Build flask api 
14) Documenting work



## Code and Resources Used 
Python Version:
Used Packages:
Requirements install:

## Dataset 
....

## Data Cleaning
I needed to clean the data up so that it was usable for our model. I made the following changes.
.....

## Exploring Data Analysis
I looked at the distribution of the data and the value counts for the various categorical variable. 
After that, I studied the relationships and the correlations between features. 
Below are a few highlights from the dataset. 
.....

## Model Building
First, I transformed the continuous variable into 2 categorics (bad/good wines). After that, I splitted the data into train and tests set with a test size of 20 %.
Ofcourse I normalized the train & test set. 

ook pca 

I tried .. different models and evaluated them and using the accuraty and f1 score, ...


## Model Preformance
The ..... model is by far the best performing model. 

models....

## Productionization
In this step, I built a Flask API endpoint that was hosted on a local webserver. 
The API Endpoint takes a request with a list of values from a wine and returns the estimated  class.

