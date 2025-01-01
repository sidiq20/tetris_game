import json

class UserProfile:
    FILE_path = "profiles.jsn"

    @staticmethod
    def load():
        try:
            with open