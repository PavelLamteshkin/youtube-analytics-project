import os
from googleapiclient.discovery import build
import json

class Channel:

    """Класс для ютуб-канала"""

    api_key = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey='AIzaSyApgQ2Fl18ga8EA2Yegx5CAkWcJPhvsFAg')

    # Функция build из googleapiclient.discovery позволяет создать ресурс для обращения к API,
    # то есть это некая абстракция над REST API Drive, чтобы удобнее обращаться к методам API.


    def __init__(self, channel_id: str) -> None:

        self.channel_id = channel_id


    def print_info(self) -> None:

        """Выводит в консоль информацию о канале в JSON."""

        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(channel, indent=2, ensure_ascii=False))
