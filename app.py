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
blue = st.selectbox("Bluetooth Supported?", [0, 1])
clock_speed = st.slider("Clock Speed (GHz)", 0.5, 3.0, 2.0)
dual_sim = st.selectbox("Dual SIM?", [0, 1])
fc = st.slider("Front Camera (MP)", 0, 20, 5)
four_g = st.selectbox("4G Supported?", [0, 1])
int_memory = st.number_input("Internal Memory (GB)", min_value=2, max_value=128, value=32)
m_dep = st.slider("Mobile Depth (cm)", 0.1, 1.0, 0.5)
mobile_wt = st.number_input("Mobile Weight (grams)", min_value=80, max_value=250, value=150)
n_cores = st.slider("Number of Cores", 1, 8, 4)
pc = st.slider("Primary Camera (MP)", 0, 20, 8)
px_height = st.number_input("Pixel Height", min_value=0, max_value=1960, value=600)
px_width = st.number_input("Pixel Width", min_value=0, max_value=1998, value=800)
ram = st.number_input("RAM (MB)", min_value=512, max_value=8000, value=3000)
sc_h = st.slider("Screen Height (cm)", 5, 20, 12)
sc_w = st.slider("Screen Width (cm)", 2, 10, 7)
talk_time = st.slider("Talk Time (Hours)", 2, 20, 15)
three_g = st.selectbox("3G Supported?", [0, 1])
touch_screen = st.selectbox("Touch Screen?", [0, 1])
wifi = st.selectbox("WiFi Supported?", [0, 1])

# Predict button
if st.button("Predict Price Range"):
    input_data = pd.DataFrame([[
        battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory,
        m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram,
        sc_h, sc_w, talk_time, three_g, touch_screen, wifi
    ]], columns=[
        'battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g', 'int_memory',
        'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram',
        'sc_h', 'sc_w', 'talk_time', 'three_g', 'touch_screen', 'wifi'
    ])

    prediction = model.predict(input_data)[0]
    categories = ["Low", "Medium", "High", "Very High"]
    st.success(f"📊 Predicted Price Range: **{categories[prediction]}**")
