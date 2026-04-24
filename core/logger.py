import json
import datetime

def save_log(question, difficulty, confusion):
    entry={
        "question": question,
        "difficulty": difficulty,
        "confusion": confusion,
        "timestamp": str(datetime.datetime.now())
    }

    with open("log.json", "a") as f:
        f.write(json.dumps(entry) + "\n")