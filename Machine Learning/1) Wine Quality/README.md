# Red Wine Quality 



## Code and Resources Used 
**Python Version**: 3.8

**Requirements packages install**: requirements.txt

## Dataset 
https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009

## Summary Project
The datasets are related to red variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification tasks (good/bad). The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).

Input variables (based on physicochemical tests): 1 - fixed acidity 2 - volatile acidity 3 - citric acid 4 - residual sugar 5 - chlorides 6 - free sulfur dioxide 7 - total sulfur dioxide 8 - density 9 - pH 10 - sulphates 11 - alcohol Output variable (based on sensory data): 12 - quality (score between 0 and 10)

## 1) Problem Understanding
The goal of this project is:
  - to understand which features makes it a good wine
  - to predict if a wine is bad or a good wine (binairy classes)

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

