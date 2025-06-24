import json
import requests

def call_llm_ollama(prompt, model='mistral'):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()['response']

def generate_meal_plan(user_profile):
    prompt = f"""
You are a certified nutritionist. Create a 1-day vegetarian meal plan based on this user profile:

Age: {user_profile['age']}
Weight: {user_profile['weight']} kg
Height: {user_profile['height']} cm
Activity level: {user_profile['activity_level']}
Goal: {user_profile['goal']}
Dietary preference: {user_profile['diet']}

Include:
- Breakfast, Lunch, Dinner, and Snacks
- Approximate calories per meal
- Hydration reminders
- Tips on fiber, electrolytes

Return the plan in clean markdown format.
"""
    return call_llm_ollama(prompt)
