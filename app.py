import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

# Title and description
st.title("📱 Mobile Price Range Predictor")
st.write("Enter mobile specifications below to predict its price category.")

# Input fields
battery_power = st.number_input("Battery Power (mAh)", min_value=500, max_value=2000, value=1200)
ram = st.number_input("RAM (MB)", min_value=512, max_value=8000, value=3000)
px_height = st.number_input("Pixel Height", min_value=0, max_value=1960, value=600)
px_width = st.number_input("Pixel Width", min_value=0, max_value=1998, value=800)

# Add more inputs as needed
fc = st.slider("Front Camera (MP)", 0, 20, 5)
pc = st.slider("Primary Camera (MP)", 0, 20, 8)
talk_time = st.slider("Talk Time (Hours)", 2, 20, 15)

# Predict button
if st.button("Predict Price Range"):
    input_data = pd.DataFrame([[battery_power, ram, px_height, px_width, fc, pc, talk_time]],
        columns=['battery_power', 'ram', 'px_height', 'px_width', 'fc', 'pc', 'talk_time'])
    
    prediction = model.predict(input_data)[0]
    
    # Map prediction to category
    categories = ["Low", "Medium", "High", "Very High"]
    st.success(f"📊 Predicted Price Range: **{categories[prediction]}**")
