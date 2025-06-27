import json
import requests
import re

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

def generate_fitness_plan(user_profile):
    prompt = f"""
You are a certified personal fitness trainer.

Create a 1-day beginner-friendly workout plan based on the following profile:

Age: {user_profile['age']}
Weight: {user_profile['weight']} kg
Height: {user_profile['height']} cm
Activity Level: {user_profile['activity_level']}
Fitness Goal: {user_profile['goal']}
Muscle Focus: {user_profile['muscle_focus']}

Return your answer as a **JSON object** with two keys:

1. `"plan"` — a list of workout steps as dictionaries. Each dictionary must include:
   - "Phase" (e.g., Warm-up, Main Workout, Cool-down)
   - "Exercise" (e.g., Jumping Jacks)
   - "Duration" (e.g., 10 mins)
   - "Notes" (brief tip, e.g., 'Maintain good form')

2. `"tips"` — a list of 5 bullet-point workout tips (e.g., about hydration, safety, consistency)

Respond with only valid JSON. No markdown, no comments, no code fences.

"""
    response = call_llm_ollama(prompt)
    # Remove any Markdown-style code blocks (```json ... ```)
    cleaned_response = re.search(r"\{[\s\S]*\}", response)
    if cleaned_response:
        json_str = cleaned_response.group()
        try:
            return json.loads(json_str)
        except Exception as e:
            return {
                "plan": [{"Phase": "Error", "Exercise": f"JSON decode error: {e}", "Duration": "", "Notes": ""}],
                "tips": []
            }
    else:
        return {
            "plan": [{"Phase": "Error", "Exercise": "No valid JSON object found in response", "Duration": "", "Notes": ""}],
            "tips": []
        }
