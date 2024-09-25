import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Title of the app
st.title("Fire Weather Index (FWI) Prediction")

@st.dialog("Fire Weather Index (FWI) Prediction")
def predict():
    # For now, we'll just display the inputs as an example
    st.write("Input Parameters:")
    st.write(f"Temperature: {temp} °C")
    st.write(f"Relative Humidity: {rh} %")
    st.write(f"Wind Speed: {ws} km/h")
    st.write(f"Rain: {rain} mm")
    st.write(f"FFMC: {ffmc}")
    st.write(f"DMC: {dmc}")
    st.write(f"DC: {dc}")
    st.write(f"ISI: {isi}")
    st.write(f"BUI: {bui}")

    st.write(f"The model you have selected is: {model_name}")
    print("", type(temp))
    input_data = np.array([[temp, rh, ws, rain, ffmc, dmc, dc, isi, bui]])
    
    # Load the StandardScaler from the pickle file
    with open('model/scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    if model_name == "Linear Regression":
        model_path = "model/linear.pkl"
    elif model_name == "Lasso Regression":
        model_path = "model/lasso.pkl"
    elif model_name == "Ridge Regression":
        model_path = "model/ridge.pkl"
    elif model_name == "Elastic Regression":
        model_path = "model/elastic.pkl"

    # Load the trained model from the pickle file
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Scale the input data using the loaded StandardScaler
    scaled_input = scaler.transform(input_data)

    # Use the loaded model to predict the FWI
    prediction = model.predict(scaled_input)
    st.write(f"Predicted Fire Weather Index (FWI): {prediction[0]:.2f}")


# Input fields for each parameter
temp = st.number_input('Temperature (°C)', min_value=22.0, max_value=42.0, value=30.0, step=0.1)
rh = st.number_input('Relative Humidity (%)', min_value=21, max_value=90, value=50, step=1)
ws = st.number_input('Wind Speed (km/h)', min_value=6, max_value=29, value=15, step=1)
rain = st.number_input('Rain (mm)', min_value=0.0, max_value=16.8, value=0.0, step=0.1)

ffmc = st.number_input('Fine Fuel Moisture Code (FFMC)', min_value=28.6, max_value=92.5, value=85.0, step=0.1)
dmc = st.number_input('Duff Moisture Code (DMC)', min_value=1.1, max_value=65.9, value=30.0, step=0.1)
dc = st.number_input('Drought Code (DC)', min_value=7.0, max_value=220.4, value=100.0, step=0.1)
isi = st.number_input('Initial Spread Index (ISI)', min_value=0.0, max_value=18.5, value=5.0, step=0.1)
bui = st.number_input('Buildup Index (BUI)', min_value=1.1, max_value=68.0, value=40.0, step=0.1)

model_name = st.selectbox(
    "Which model would you like to use?",
    ("Linear Regression", "Lasso Regression", "Ridge Regression", "Elastic Regression"),
    index=None,
    placeholder="Select model...",
)

st.write("You have selected:", model_name)

# Check if any input is missing
inputs_filled = all([
    temp is not None,
    rh is not None,
    ws is not None,
    rain is not None,
    ffmc is not None,
    dmc is not None,
    dc is not None,
    isi is not None,
    bui is not None,
    model_name is not None,
])

# Button to submit the form
if st.button('Predict FWI', disabled=not inputs_filled):
    predict()

# Display a message if the button is inactive
if not inputs_filled:
    st.write("Please fill out all the inputs to enable the prediction.")
