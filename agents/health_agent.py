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
You are a certified nutritionist. Create a 1-day meal plan in **JSON format** based on the following user profile:

Age: {user_profile['age']}
Weight: {user_profile['weight']} kg
Height: {user_profile['height']} cm
Activity level: {user_profile['activity_level']}
Goal: {user_profile['goal']}
Dietary preference: {user_profile['diet']}

Return a list of dictionaries like:
[
  {{
    "Meal": "Breakfast",
    "Items": "Oats, Banana, Almonds",
    "Calories": 350,
    "Nutrients": "Carbs: 45g, Protein: 10g, Fat: 12g"
  }},
  ...
]

Also, return a separate list of 5 bullet-point tips as a JSON list called `tips`.

Final format:
{{
  "plan": [...],
  "tips": [...]
}}
Only return this JSON. No markdown or explanation.

"""
    # return call_llm_ollama(prompt)
    response = call_llm_ollama(prompt)
    try:
        return json.loads(response.strip())
    except Exception as e:
        return {"plan": [{"Meal": "Error", "Items": str(e), "Calories": "", "Nutrients": ""}], "tips": []}
