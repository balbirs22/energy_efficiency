from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

models_dir = os.path.join(os.getcwd(), "energy_efficiency\models")

try:
    with open(os.path.join(models_dir, "heat_model.pkl"), "rb") as heat_file:
        heat_model = pickle.load(heat_file)
except FileNotFoundError:
    print("Error: 'models/heat_model.pkl' not found.")
    heat_model = None

try:
    with open(os.path.join(models_dir, "cool_model.pkl"), "rb") as cool_file:
        cool_model = pickle.load(cool_file)
except FileNotFoundError:
    print("Error: 'models/cool_model.pkl' not found.")
    cool_model = None


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_heat', methods=['GET', 'POST'])
def predict_heat():
    if request.method == 'POST':
        try:
            # Get input values for heat prediction
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
            prediction = heat_model.predict(np.array([inputs])) if heat_model else None
            return str(round(prediction[0], 2)) if prediction is not None else "Error: Model not loaded."
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('heat.html')


@app.route('/predict_cool', methods=['GET', 'POST'])
def predict_cool():
    if request.method == 'POST':
        try:
            # Get input values for cool prediction
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
            prediction = cool_model.predict(np.array([inputs])) if cool_model else None
            return str(round(prediction[0], 2)) if prediction is not None else "Error: Model not loaded."
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('cool.html')

if __name__ == "__main__":
    app.run(debug=True)