import json

STOPWORDS = {
    "i", "am", "is", "are", "the", "a", "an", "can", "cannot",
    "never", "think", "this", "that", "it", "to", "of", "in"
}

def analyze_logs():
    topic_count = {}
    difficulty_map = {}

    try:
        with open("log.json", "r") as f:
            for line in f:
                entry = json.loads(line)

                question = entry.get("question", "").lower()
                confusion = entry.get("confusion", "").lower()
                difficulty = int(entry.get("difficulty", 0))

                text = question + " " + confusion

                words = text.split()

                for word in words:
                    word = word.strip(",.!?")

                    if word in STOPWORDS or len(word) <= 2:
                        continue

                    if word not in topic_count:
                        topic_count[word] = 0
                        difficulty_map[word] = 0

                    topic_count[word] += 1
                    difficulty_map[word] += difficulty

    except FileNotFoundError:
        return {"error": "No logs found."}

    weak_topics = []

    for word in topic_count:
        avg_difficulty = difficulty_map[word] / topic_count[word]

        if avg_difficulty >= 3:
            weak_topics.append((word, round(avg_difficulty, 2)))

    weak_topics.sort(key=lambda x: x[1], reverse=True)

    return weak_topics[:5]
       
                