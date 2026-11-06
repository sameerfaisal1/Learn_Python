import json

data = {
    "name": "Ali",
    "skills": ["Python", "SQL"]
}

with open("ali.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)