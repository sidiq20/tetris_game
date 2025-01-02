import json

class UserProfile:
    FILE_PATH = "profiles.json"

    @staticmethod
    def load():
        try:
            with open(UserProfile.FILE_PATH, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save(profiles):
        with open(UserProfile.FILE_PATH, "w") as file:
            json.dump(profiles, file)

    @staticmethod
    def get_profile(name):
        profiles = UserProfile.load()
        return profiles.get(name, {"name": name, "high_score": 0})

    @staticmethod
    def update_profile(name, score):
        profiles = UserProfile.load()
        if name not in profiles or score > profiles[name]["high_score"]:
            profiles[name] = {"name": name, "high_score": score}
        UserProfile.save(profiles)

    @staticmethod
    def delete_profile(name):
        profiles = UserProfile.load()
        if name in profiles:
            del profiles[name]
            UserProfile.save(profiles)