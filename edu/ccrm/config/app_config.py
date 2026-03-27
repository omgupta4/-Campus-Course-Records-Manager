# edu/ccrm/config/app_config.py

import configparser
import os

class AppConfig:
    _instance = None  # Singleton instance

    def __init__(self):
        # Default values
        self._student_file = "students.csv"
        self._course_file = "courses.csv"
        self._backup_folder = "backups"
        self._max_credits = 18

        config = configparser.ConfigParser()

        try:
            if os.path.exists("config.properties"):
                config.read("config.properties")

                if "DEFAULT" in config:
                    props = config["DEFAULT"]

                    self._student_file = props.get("studentFile", self._student_file)
                    self._course_file = props.get("courseFile", self._course_file)
                    self._backup_folder = props.get("backupFolder", self._backup_folder)
                    self._max_credits = int(props.get("maxCredits", self._max_credits))
            else:
                print("⚠ No config.properties found, using defaults.")

        except Exception:
            print("⚠ Error reading config.properties, using defaults.")

    # Singleton access method
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = AppConfig()
        return cls._instance

    # Getters
    @property
    def student_file(self):
        return self._student_file

    @property
    def course_file(self):
        return self._course_file

    @property
    def backup_folder(self):
        return self._backup_folder

    @property
    def max_credits(self):
        return self._max_credits