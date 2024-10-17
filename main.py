from flask import Flask, render_template, request
import numpy as np
import pickle
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb

app = Flask(__name__)

models_dir = os.path.join(os.getcwd(), "energy_efficiency/models")
data_file = "energy_efficiency/energy_efficiency_dataset.csv"

df = pd.read_csv(data_file)
print(df.columns)
df.rename(columns={
        'X1': 'Relative_Compactness', 'X2': 'Surface_Area', 'X3': 'Wall_Area', 
        'X4': 'Roof_Area', 'X5': 'Overall_Height', 'X6': 'Orientation', 
        'X7': 'Glazing_Area', 'X8': 'Glazing_Area_Distribution', 
        'Y1': 'Heating_Load', 'Y2': 'Cooling_Load'}, inplace=True)
print(df.columns)
try:
    with open(os.path.join(models_dir, "heat_model.pkl"), "rb") as heat_file:
        heat_model = pickle.load(heat_file)
except FileNotFoundError:
    heat_model = None

try:
    with open(os.path.join(models_dir, "cool_model.pkl"), "rb") as cool_file:
        cool_model = pickle.load(cool_file)
except FileNotFoundError:
    cool_model = None

def save_data(inputs, heat, cool):
    new_data = pd.DataFrame([inputs + [heat, cool]], columns=['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'Y1', 'Y2'])
    with open(data_file, mode='a', newline='') as file:
        new_data.to_csv(file, header=False, index=False)


def retrain_models():
    X = df[['Relative_Compactness', 'Surface_Area', 'Wall_Area', 'Roof_Area', 'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Area_Distribution']]
    y_heat = df['Heating_Load']
    y_cool = df['Cooling_Load']

    X_train_heat, X_test_heat, y_train_heat, y_test_heat = train_test_split(X, y_heat, test_size=0.2, random_state=42)
    X_train_cool, X_test_cool, y_train_cool, y_test_cool = train_test_split(X, y_cool, test_size=0.2, random_state=42)

    heat_model_xgb = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    heat_model_xgb.fit(X_train_heat, y_train_heat)

    cool_model_xgb = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)
    cool_model_xgb.fit(X_train_cool, y_train_cool)

    with open(os.path.join(models_dir, "heat_model.pkl"), "wb") as heat_file_xgb:
        pickle.dump(heat_model_xgb, heat_file_xgb)

    with open(os.path.join(models_dir, "cool_model.pkl"), "wb") as cool_file_xgb:
        pickle.dump(cool_model_xgb, cool_file_xgb)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_heat', methods=['GET', 'POST'])
def predict_heat():
    if request.method == 'POST':
        try:
            inputs = [
                float(request.form.get('Relative_Compactness')),
                float(request.form.get('Surface_Area')),
                float(request.form.get('Wall_Area')),
                float(request.form.get('Roof_Area')),
                float(request.form.get('Overall_Height')),
                float(request.form.get('Orientation')),
                float(request.form.get('Glazing_Area')),
                float(request.form.get('Glazing_Area_Distribution'))
            ]

            heat_prediction = heat_model.predict(np.array([inputs]))[0] if heat_model else None
            cool_prediction = cool_model.predict(np.array([inputs]))[0] if cool_model else None

            save_data(inputs, heat_prediction, cool_prediction)
            retrain_models()

            return str(round(heat_prediction, 2)) if heat_prediction is not None else "Error: Heat model not loaded."
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('heat.html')

@app.route('/predict_cool', methods=['GET', 'POST'])
def predict_cool():
    if request.method == 'POST':
        try:
            inputs = [
                float(request.form.get('Relative_Compactness')),
                float(request.form.get('Surface_Area')),
                float(request.form.get('Wall_Area')),
                float(request.form.get('Roof_Area')),
                float(request.form.get('Overall_Height')),
                float(request.form.get('Orientation')),
                float(request.form.get('Glazing_Area')),
                float(request.form.get('Glazing_Area_Distribution'))
            ]

            cool_prediction = cool_model.predict(np.array([inputs]))[0] if cool_model else None
            heat_prediction = heat_model.predict(np.array([inputs]))[0] if heat_model else None

            save_data(inputs, heat_prediction, cool_prediction)
            retrain_models()

            return str(round(cool_prediction, 2)) if cool_prediction is not None else "Error: Cool model not loaded."
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('cool.html')

if __name__ == "__main__":
    app.run(debug=True)
