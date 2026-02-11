import configparser
import os

config = configparser.ConfigParser()

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(base_path, "config", "config.ini")

config.read(config_path)

def get_url():
    return config.get("settings", "url")