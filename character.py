import requests

class InworldCharacter:
    BASE_URL = "https://studio.inworld.ai/v1/"

    def __init__(self, api_key, workspace, character_name, user):
        self.api_key = api_key
        self.workspace = workspace
        self.character_name = character_name
        self.user = user
        self.session_id = None
        self.character_id = None

    def open_session(self):
        url = f'{self.BASE_URL}{self.workspace}/characters/{self.character_name}:openSession'
        headers = {"Content-Type": "application/json", "authorization": self.api_key}
        response = requests.post(url, json={"name": f"{self.workspace}/characters/{self.character_name}", "user": self.user}, headers=headers)
        data = response.json()
        self.session_id = data["name"]
        self.character_id = data['sessionCharacters'][0]['character']

    def send_text(self, message):
        url = f'{self.BASE_URL}{self.workspace}/sessions/{self.session_id}/sessionCharacters/{self.character_id}:sendText'
        headers = {"Content-Type": "application/json", "authorization": self.api_key, "Grpc-Metadata-session-id": self.session_id}
        response = requests.post(url, json={"text": message}, headers=headers)
        return " ".join(response.json()["textList"])