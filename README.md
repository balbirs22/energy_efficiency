# Energy Load Prediction

## About

This project is a web application designed to predict the **Heating Load** and **Cooling Load** of a building based on various input parameters such as Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, and Glazing Area Distribution. The models for **Heating Load** and **Cooling Load** are built using machine learning techniques, including ensemble learning methods, and are served via a Flask web application. The system dynamically retrains the models with new user inputs to continuously improve prediction accuracy.

## Features

- Predicts **Heating Load** and **Cooling Load** separately using trained machine learning models.
- Implements **Ensemble Learning** with **Random Forest** and **XGBoost** for more accurate predictions.
- User-friendly interface for inputting building parameters.
- Real-time predictions displayed on the web app.
- Retrains models automatically with new data entered by users.
- Separate pages for **Heating Load** and **Cooling Load** predictions.
- Responsive design using Bootstrap.

## Input Parameters

- **Relative Compactness**: Decimal value representing the ratio of volume to surface area.
- **Surface Area**: Total exterior surface area of the building (in m²).
- **Wall Area**: Surface area of the walls (in m²).
- **Roof Area**: Surface area of the roof (in m²).
- **Overall Height**: The overall height of the building (in meters).
- **Orientation**: Numeric representation of the building's orientation (1-4).
- **Glazing Area**: The total area covered by windows (in m²).
- **Glazing Area Distribution**: Distribution of the glazing area (1-5).

## Ensemble Learning

This project uses two ensemble learning techniques for prediction:

1. **Random Forest**: A robust ensemble learning method that combines multiple decision trees to improve predictive performance.
2. **XGBoost**: An optimized version of gradient boosting that is faster and provides better accuracy for structured data.

## Dynamic Model Retraining

When a user submits data through the web application, the new input is:

1. **Saved** in the original CSV file (as new rows).
2. **Retrained**: The Random Forest and XGBoost models are automatically retrained to include the newly added data, allowing the models to learn and improve over time.

This feature ensures that the models remain up-to-date and can adapt to any new trends in the data.


## Project Structure

```plaintext
|-- models/                # Directory containing pre-trained machine learning models
|   |-- heat_model.pkl      # Pickle file for heat load prediction model
|   |-- cool_model.pkl      # Pickle file for cool load prediction model
|-- static/                # Static files (CSS, images)
|   |-- css/               # CSS files for the web pages
|   |-- cool.css
|   |-- heat.css
|   |-- home.css
|-- templates/             # HTML templates
|   |-- home.html          # Main landing page
|   |-- heat.html          # Page for predicting heating load
|   |-- cool.html          # Page for predicting cooling load
|-- energy_efficiency.ipynb # Jupyter notebook for model training and retraining
|-- main.py                # Flask application
|-- energy_efficiency_dataset.csv               # CSV file containing building data used for training
|-- README.md              # Project documentation