**Report of Flight Price Prediction using Machine Learning using Machine learning methods**

**Abstract**

**1. Information gathering**

The dataset contains 25 features with 4287 records. The dataset is about the prices of the flights for various airlines based on some features and conditions. Nowadays, it is difficult to predict the optimal time to buy the ticket with a minimum price since prices change dynamically due to different conditions. As a result of that, we use machine learning to fix the problem to help customers predict the optimal time to buy a ticket with minimum price

**2. Data Attributes:**

**Out\_Date, Out\_Day, Out\_Weekday, Out\_Month, out\_Year:** The date when the journey starts from the source.

**Out\_Time:** The time when the journey starts from the source

**Out\_Cities**: The city at which the journey starts from the source

**Out\_Airline:** The name of the airline when the journey travels only to the destination

**Return\_Date, Return\_Day, Return\_Weekday, Return\_Month, Return\_Year**: The date when someone travels back to its source

**Return\_Time:** The time when the journey travels back the source

**Return\_Cities**: The city at which the journey travels back to the source

**Return\_Airline:** The name of the airline when the journey travels back to the sources

**Out\_Travel\_Time:** Total duration of the flight to travel only to the destination

**Return\_Travel\_Time:** Total duration of the flight to travel back to the source

**Out\_Journey\_Type** The type of the journey during travelling to the destination. It could be direct or connecting

**Return\_Journey\_Type:** The type of the journey during travelling back to the source. It could be direct connecting

**Out\_Stop\_Cities:** The number of intermediate stops of the journey during travelling to the destination

**Return\_Stop\_Cities:** The number of intermediate stops of the journey during travelling to the source

**Price**: The price of the ticket

**timestamp**: The date and time for webscarpping the information from the website

**sort**: sorting based on the quality of the flight journey.

**Task**

The application is a simple flight price prediction which uses a ML trained model to predict the optimal time to buy a ticket with minimum price by using such prediction a customer can buy the minimum priced ticket within optimal time

**Exploratory Data Analysis and Feature Extraction:**

We started with reading the dataset and using basic code to visualise the columns, its data types. 

a. Data Selection.

b. Data Pre-processing.

c. Data Visualization.

d. Transform data (scale, normalize the data, dimensionality reduction)

e. Data Sampling

**2. Modelling**

In Project we used Linear Regression method from sklearn linear model and Random Forest as first and second algorithm respectively to train our data set

**Feature Importance**

**Observations:**

- Like what we have done int the Out\_Travel\_Time attribute when we split it into two attributes one for the hours part and the second one for the minutes one
- We also apply this procedure two the Dep\_Time and Arrival\_Time attributes



**Out\_Date, Return\_Date**

- We can see both them are splitted into three separate columns Day, Month, Year (removed)
- So these two columns don't give us extra information, so we can remove them

**Out\_Travel\_Time and Return\_Travel\_Time**

- We can split the Out\_Travel\_Time attribute into hours and minutes
- From Data Exploration part, we can see that we don't need all the time attributes corresponds to the returning time

**Out\_Time**

- We can see that Out\_Time attribute consists of departure time and arrival time
- Departure time is the time the flight leaves the source
- Arrival time is the time the flight reaches the destination
- So we can split this attibutes into two which is Arr\_Time and Dep\_Time

**Return\_Airline**

- For this column, we can get rid of it since it is an irrelevant feature because what information we get if for predicting the optimal price with minimum time if we know the return airlines

**Observations:**

- We can that Out\_Journey\_Type is a ordinal data where every class in this variable have a specific level of importance.
- as we can see direct means 0, connected means one or more stops
- Since the data is ordinal, we will use label encoder

**Performance of models and Conclusion**

After training the model we tested the model on our validation data. We got the accuracy of 96.5%. For Model's Performance Analysis we used R2 score analyse the performance of our model

**Design** 

- **Data**
- The dataset contains 25 features with 4287 records. The dataset is about the prices of the flights for various airlines based on some features and conditions.
- **Data Pre-processing**
- Checking for missing values and changing for datatypes if needed

- **EDA**
- Distribution outliers and skewness of each attribute. Correlation between each attribute to get a better inference. Data Visualization for Understanding of each feature.

- **Training Model:** 
- Applying Linear Regression, and SVM for prediction by dividing the data into test train split.

- **Test Model & Evaluation:**
- Comparing all the models applied. Prediction will be done. Checking for accuracy Score (Overfitting, Underfitting) if exists.

- **Model deployment:**
- Deploy the model and check the functionality.

**Implementation**

We tried to predict the model accuracy the help of two models --- Linear Regression and Random Forest

**Linear Regression**

You’re probably familiar with plotting [line graphs](https://www.statisticshowto.com/line-graph/) with one X axis and one Y axis. The X variable is sometimes called the [independent variable](https://www.statisticshowto.com/independent-variable-definition/) and the Y variable is called the [dependent variable](https://www.statisticshowto.com/dependent-variable-definition/). Simple linear regression plots one independent variable X against one dependent variable Y. Technically, in regression analysis, the independent variable is usually called the [predictor variable](https://www.statisticshowto.com/independent-variable-definition/#Predictor) and the dependent variable is called the [criterion variable](https://www.statisticshowto.com/criterion-variable-2/). However, many people just call them the independent and dependent variables. More advanced regression techniques (like [multiple regression](https://www.statisticshowto.com/probability-and-statistics/regression-analysis/#MRA)) use multiple independent variables.

**Random Forest**

Random forests or random decision forests are **an ensemble learning method for classification, regression and other tasks** that operates by constructing a multitude of decision trees at training time. Random forests generally outperform decision trees, but their accuracy is lower than gradient boosted trees


**Deployment**

The model deployment part was divided into two parts:

- Model using Linear Regression: Deployment through Python Flask
- Model using: Deployment through Django.

***Deployment Model using Linear Regression for Prediction.***

**Flight Price Prediction** **Application**

The application is a Flight Price Prediction application which uses a ML trained model to predict the optimal time and flight ticket price so that a person can book a ticket accordingly. 

**Description of the web application**

The web application uses simple techniques for its implementation.

- **HTML & CSS** for the frontend part.
- **Flask** is used in backend.

**Workflow of the project**

The main file that we need to focus on is **app.py**.

**STEP 1:** We have done necessary imports of the library that we need to implement our logic.

**STEP 2:** After that we read the pickled file.

**STEP 3:** The user inputs necessary data into the form like structure and once click the submit button the result is displayed on the screen itself
###
###
###
###
###
### **Screenshot of the project**


Result for the prediction


***Deployment Link for Model***




