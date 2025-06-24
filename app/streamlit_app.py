import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.health_agent import generate_meal_plan

st.title("🥗 AI Health & Fitness Planner")
st.subheader("Personalized Diet Plan Generator")

with st.form("user_profile_form"):
    age = st.number_input("Age", min_value=10, max_value=100)
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Moderately Active", "Very Active"])
    goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"])
    diet = st.selectbox("Dietary Preference", ["Vegetarian", "Keto", "Low-Carb", "Balanced"])
    submitted = st.form_submit_button("Generate Meal Plan")

if submitted:
    user_profile = {
        "age": age,
        "weight": weight,
        "height": height,
        "activity_level": activity_level,
        "goal": goal,
        "diet": diet
    }
    st.info("Generating your personalized meal plan...")
    plan = generate_meal_plan(user_profile)
    st.markdown(plan)
