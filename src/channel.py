import os
from googleapiclient.discovery import build
import json


class Channel:

    """Класс для ютуб-канала"""

    api_key = os.getenv('YOUTUBE_API_KEY')


    def __init__(self, channel_id) -> None:

        self.channel_id = channel_id

        channel = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = channel['items'][0]['snippet']['title']
        self.description = channel['items'][0]['snippet']['description']
        # self.url = channel['items'][0]['snippet']['thumbnails']['default']['url']
        self.url = 'https://www.youtube.com/channel/' + self.channel_id
        self.subscriber_count = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']


    def __str__(self):
        return f'{self.title} ({self.url})'


    @classmethod
    def get_service(cls):
        """
        Метод возвращает объект для работы с YouTube API
        """

        youtube = build('youtube', 'v3', developerKey=cls.api_key)

        return youtube


    def to_json(self, jason_file):
        """
        Метод сохраняет в файл значения атрибутов экземпляра
        """

        data = {"title": self.title,
                "description": self.description,
                "url": self.url,
                "subscriber_count": self.subscriber_count,
                "video_count": self.video_count,
                "view_count": self.view_count
                }

        with open(jason_file, 'w') as outfile:
            json.dump(data, outfile)

        return data


    def print_info(self, data):

        return json.dumps(data, indent=2, ensure_ascii=False)


    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)


    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)


    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)


    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)


    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)


    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)


    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)
