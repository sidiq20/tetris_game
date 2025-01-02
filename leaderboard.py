import json

class Leaderboard:
    FILE_PATH = "leaderboard.json"

    @staticmethod
    def load():
        try:
            with open(Leaderboard.FILE_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save(data):
        with open(Leaderboard.FILE_PATH, "w") as file:
            json.dump(data, file)

    @staticmethod
    def add_score(name, score):
        data = Leaderboard.load()
        data.append({"name": name, "score": score})
        data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
        Leaderboard.save(data)

    @staticmethod
    def print_leaderboard():
        scores = Leaderboard.load()
        print("Leaderboard:")
        for i, entry in enumerate(scores, 1):
            print(f"{i}. {entry['name']} - {entry['score']}")