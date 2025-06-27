import streamlit as st
import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents.health_agent import generate_meal_plan
from agents.fitness_agent import generate_fitness_plan
from app.utils import generate_pdf


st.title("💪 AI Health & Fitness Planner")

tab1, tab2 = st.tabs(["🥗 Diet Plan", "🏋️ Fitness Plan"])

with tab1:
    st.subheader("Generate a Personalized Meal Plan")
    with st.form("diet_form"):
        age = st.number_input("Age", min_value=10, max_value=100, key="diet_age")
        weight = st.number_input("Weight (kg)", key="diet_weight")
        height = st.number_input("Height (cm)", key="diet_height")
        activity_level = st.selectbox("Activity Level", ["Sedentary", "Moderately Active", "Very Active"], key="diet_activity")
        goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"], key="diet_goal")
        diet = st.selectbox("Diet Type", ["Vegetarian", "Keto", "Low-Carb", "Balanced"], key="diet_type")
        submitted = st.form_submit_button("Generate Diet Plan")

    if submitted:
        profile = {
            "age": age,
            "weight": weight,
            "height": height,
            "activity_level": activity_level,
            "goal": goal,
            "diet": diet
        }
        st.info("Generating your diet plan...")
        meal_plan = generate_meal_plan(profile)
        # Show table
        st.subheader("Your Meal Plan")
        st.table(pd.DataFrame(meal_plan["plan"]))

        # Show tips
        st.subheader("Tips")
        for tip in meal_plan["tips"]:
            st.markdown(f"- {tip}")

        pdf_path = generate_pdf(meal_plan, title="Personalised Meal Plan")
        with open(pdf_path, "rb") as f:
            st.download_button("📄 Download Meal Plan as PDF", f, "meal_plan.pdf", "application/pdf")

with tab2:
    st.subheader("Generate a Personalized Fitness Plan")
    with st.form("fitness_form"):
        age = st.number_input("Age", min_value=10, max_value=100, key="fitness_age")
        weight = st.number_input("Weight (kg)", key="fitness_weight")
        height = st.number_input("Height (cm)", key="fitness_height")
        activity_level = st.selectbox("Activity Level", ["Sedentary", "Moderately Active", "Very Active"], key="fitness_activity")
        goal = st.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Maintenance"], key="fitness_goal")
        muscle_focus = st.selectbox("Muscle Focus", ["Upper Body", "Lower Body", "Shoulders", "Arms", "Glutes"], key="muscle_focus")
        submitted = st.form_submit_button("Generate Fitness Plan")

    if submitted:
        profile = {
            "age": age,
            "weight": weight,
            "height": height,
            "activity_level": activity_level,
            "goal": goal,
            "muscle_focus": muscle_focus
        }
        st.info("Generating your fitness plan...")
        workout_plan = generate_fitness_plan(profile)
        # Show table
        st.subheader("Your Workout Plan")
        st.table(pd.DataFrame(workout_plan["plan"]))

        # Show tips
        st.subheader("Tips")
        for tip in workout_plan["tips"]:
            st.markdown(f"- {tip}")

        pdf_path = generate_pdf(workout_plan, title="Personalized Fitness Plan")
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📄 Download Fitness Plan as PDF",
                data=f,
                file_name="fitness_plan.pdf",
                mime="application/pdf"
            )
