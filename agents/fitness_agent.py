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

Output the plan in a tabular format with the following columns:
| Phase | Exercise | Duration | Notes |

Phases include: Warm-up, Main Workout, Cool-down.

After the table, add 5 bullet-point **tips** (e.g., safety, breathing, consistency).

"""
    return call_llm_ollama(prompt)
