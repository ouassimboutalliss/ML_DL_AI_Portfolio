# Red Wine Quality 

![monte-baixo-vinho-verde-red-2020](https://user-images.githubusercontent.com/43603147/229355343-3c43530d-ba2e-4f69-a8c5-68ad170612f2.jpg)

## Code and Resources Used 
**Python Version**: 3.8

**Requirements packages install**: requirements.txt

## Summary Project
The datasets are related to red variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).


These datasets can be viewed as classification tasks (good/bad). The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).

Input variables (based on physicochemical tests): 1 - fixed acidity 2 - volatile acidity 3 - citric acid 4 - residual sugar 5 - chlorides 6 - free sulfur dioxide 7 - total sulfur dioxide 8 - density 9 - pH 10 - sulphates 11 - alcohol Output variable (based on sensory data): 12 - quality (score between 0 and 10)

I downloaded the datset from Kaggle: https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009



## 1) Problem Understanding
The goal of this project is:
  - to understand which features make it a good wine
  - to predict if a wine is bad or good (binairy classes)

## 2) Load Dataset

In this step, I imported the dataset into the notebook.

After loading the dataset, I printed the number of rows and columns. The dataset has 1599 rows and 12 columns.


## 3) Exploring Data Analysis (before cleaning)
To begin with, I previewed the first and last five rows of the dataset to gain an understanding of the data. I then searched for any missing or NaN values, but none were found. Next, I examined the data distribution and observed the presence of numerous problematic outliers. After analyzing the distribution, I also inspected for duplicated rows.

Below are a few highlights from the dataset. 


**Distribution**: 

![stats_data_before](https://user-images.githubusercontent.com/43603147/229358659-bc1ccabe-8a4b-4289-a0f1-13e2ab74a2a4.png)


![distribution](https://user-images.githubusercontent.com/43603147/228236149-a211f1cc-e800-4b31-979d-37f759190b18.PNG)


**Duplicated  Rows**:

![duplicated_rows](https://user-images.githubusercontent.com/43603147/228237162-91c5d576-af19-44b6-bfa6-00363297b7ae.PNG)


## Data Cleaning
I needed to clean the data up so that it was usable for our model. I made the following changes.
.....

## 3) Exploring Data Analysis (before cleaning)
I looked at the distribution of the data 
After that, I studied the relationships and the correlations between features. 
Below are a few highlights from the dataset. 
.....

## Model Building
First, I transformed the continuous variable into 2 categorics (bad/good wines). After that, I splitted the data into train and tests set with a test size of 20 %.
Ofcourse I normalized the train & test set. 


This hasn't been updated.
