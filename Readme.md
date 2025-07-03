# 🧠 AI Health & Fitness Planner

The **AI Health & Fitness Planner** is a personalized wellness assistant powered by open-source LLMs (via Ollama). It generates **custom dietary and fitness plans** based on user inputs such as age, weight, height, activity level, dietary preferences, fitness goals, and muscle focus.

This is a beginner-friendly full-stack GenAI project using **Streamlit**, **Python**, and **local LLMs**. No paid APIs. No external cloud calls.


## 🚀 Features

### 🥗 Health Agent — Personalized Meal Plans
- Generates a complete 1-day **vegetarian meal plan**
- Tailored to **age, weight, height, activity level, fitness goal, and diet preference**
- Output includes:
  - Table with Meal, Items, Calories, and Nutrients
  - 5 expert **nutrition & hydration tips**
- Supports **Q&A**: Ask follow-up dietary questions in a chat interface
- Export plan as **PDF**


### 🏋️ Fitness Agent — Personalized Workout Plans
- Generates a **beginner-friendly 1-day workout routine**
- Personalized by:
  - Age, Weight, Height, Activity Level
  - Fitness Goal (e.g. Muscle Gain)
  - Muscle Focus (e.g. Arms, Glutes, etc.)
- Workout includes:
  - Warm-up, Main Workout, Cool-down phases
  - Exercise names, durations, and notes
- 5 expert **training tips**
- Supports **interactive Q&A**
- Export plan as **PDF**


## 🛠 Tech Stack

| Tool         | Purpose                                 |
|--------------|------------------------------------------|
| 🐍 Python     | Backend and core logic                   |
| 📺 Streamlit  | Interactive Web UI                      |
| 🧠 Ollama     | Local LLM runtime (no API keys needed)  |
| 🧩 Mistral    | Open-weight LLM for plan generation      |
| 📝 Requests   | HTTP calls to Ollama API                 |
| 📄 FPDF       | PDF generation for downloadable plans    |


