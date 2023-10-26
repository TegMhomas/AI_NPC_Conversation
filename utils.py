import json

class ConfigManager:
    @staticmethod
    def load_config(filename):
        with open(filename, 'r') as file:
            return json.load(file)

    @staticmethod
    def load_general_config():
        return ConfigManager.load_config('config/general_config.json')

class LogManager:
    @staticmethod
    def save_message_to_log(message, filename="logs/conversation.txt"):
        with open(filename, 'a') as file:
            file.write(message + '\n')