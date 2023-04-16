import os
from googleapiclient.discovery import build
import json


class Channel:

    """Класс для ютуб-канала"""

    def __init__(self, channel_id) -> None:

        self.channel_id = channel_id

    @classmethod
    def get_service(cls):
        """
        Метод возвращает объект для работы с YouTube API
        """

        api_key = os.getenv('YOUTUBE_API_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)

        return youtube

    @classmethod
    def to_json(cls, channel_id):
        """
        Метод сохраняет в файл значения атрибутов экземпляра
        """
        channel = cls.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        channel_json = json.dumps(channel, indent=2, ensure_ascii=False)

        return channel_json
