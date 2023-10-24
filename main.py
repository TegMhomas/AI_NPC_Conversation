import time
from utils import ConfigManager, LogManager
from character import InworldCharacter

def main():
    # Load configurations
    general_config = ConfigManager.load_general_config()
    api_key = general_config['api_key']

    characters = []
    for config_filename in general_config['character_configs']:
        char_config = ConfigManager.load_config(f"config/{config_filename}")
        char = InworldCharacter(api_key, char_config['workspace'], char_config['character_name'], char_config['user'])
        char.open_session()
        characters.append(char)

    messages = ["hello", "hi"]
    while True:
        for i in range(len(characters)):
            message = characters[i].send_text(messages[i])
            print(message)
            LogManager.save_message_to_log(message)
            messages[(i + 1) % len(characters)] = message
            time.sleep(3)

if __name__ == "__main__":
    main()