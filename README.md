# Energy Efficiency Prediction

## About

This project is a web application designed to predict the heating and cooling efficiency of a building based on various input parameters such as Relative Compactness, Surface Area, Wall Area, Roof Area, Overall Height, Orientation, Glazing Area, and Glazing Area Distribution. The models for heat and cool efficiency are built using machine learning techniques and are served via a Flask web application.

## Features

- Predicts **Heat Efficiency** and **Cool Efficiency** separately using trained machine learning models.
- User-friendly interface for inputting building parameters.
- Real-time predictions displayed on the web app.
- Separate pages for **Heat** and **Cool** predictions.
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

## Project Structure

```plaintext
|-- models/                # Directory containing pre-trained machine learning models
|   |-- heat_model.pkl      # Pickle file for heat prediction model
|   |-- cool_model.pkl      # Pickle file for cool prediction model
|-- static/                # Static files (CSS, images)
|   |-- css/               # CSS files for the web pages
|   |-- cool.css
|   |-- heat.css
|   |-- home.css
|-- templates/             # HTML templates
|   |-- home.html          # Main landing page
|   |-- heat.html          # Page for predicting heat efficiency
|   |-- cool.html          # Page for predicting cool efficiency
|-- energy_efficiency.ipynb # Jupyter notebook for model training
|-- main.py                # Flask application
|-- README.md              # Project documentation


