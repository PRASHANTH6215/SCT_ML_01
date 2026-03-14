# SCT_ML_01
Machine Learning house price prediction
# House Price Prediction using Machine Learning

## Project Overview

This project builds a **Machine Learning model** to predict house prices based on important property features such as living area, basement area, number of bathrooms, garage capacity, and overall house quality.

The model is trained using the **House Prices dataset** and deployed through a **Streamlit GUI application**, allowing users to enter house details and instantly receive a predicted house price.

This project demonstrates the complete **machine learning workflow**, including data preprocessing, model training, evaluation, and deployment.

---

## Features

* Data preprocessing and cleaning
* Feature selection based on correlation analysis
* Linear Regression model for price prediction
* Model evaluation using **R² Score and Mean Squared Error**
* Interactive **Streamlit GUI application** for user input
* Model saved using **Pickle (.pkl)** for deployment

---

## Dataset

The dataset contains housing features such as:

* Overall house quality
* Above ground living area
* Basement area
* Number of garage spaces
* Number of bathrooms

**Target variable**

* SalePrice → Final house price

Dataset files used:

* `train.csv`
* `test.csv`
* `sample_submission.csv`

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Streamlit

---

## Machine Learning Model

The project uses a **Linear Regression model** to predict house prices.

The model learns relationships between housing features and the final sale price.

Key features used for training:

* OverallQual
* GrLivArea
* GarageCars
* TotalBsmtSF
* FullBath

---

## Project Structure

```
House_Price_Prediction
│
├── train_model.ipynb
├── app.py
├── house_model.pkl
├── train.csv
├── test.csv
├── sample_submission.csv
├── submission.csv
└── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/yourusername/house-price-prediction.git
```

### 2. Install Required Libraries

```
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

### 3. Train the Model

Run the notebook:

```
train_model.ipynb
```

This will generate:

```
house_model.pkl
```

### 4. Run the GUI Application

```
streamlit run app.py
```

The application will open in your browser where you can enter house details and get a predicted price.

---

## Example Prediction Interface

Users can input:

* House quality
* Living area
* Basement size
* Garage capacity
* Number of bathrooms

The application then predicts the **estimated house price**.

---

## Learning Outcomes

This project demonstrates:

* Machine learning model development
* Feature selection and correlation analysis
* Data visualization
* Model deployment using Streamlit
* Creating user-driven applications with GUI

---

## Future Improvements

* Implement advanced models such as **Random Forest or XGBoost**
* Improve prediction accuracy
* Add more housing features
* Deploy the application online

---

## Author

Prashanth Gowda

Aspiring Software Engineer and Machine Learning Enthusiast
