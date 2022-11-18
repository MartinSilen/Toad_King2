import os

from dotenv import load_dotenv
from pymongo import MongoClient

from main.common.external.models.event import Event


class DaoEventBaseImplementation:

    def __init__(self):
        load_dotenv()
        self._DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
        self._DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
        self._DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
        self._database_name = os.getenv('DATABASE_NAME')
        self._collection_name = 'event_bases'
        self._client = MongoClient(self._DATABASE_CONNECTION_STRING, document_class=dict)

    def _get_collection(self):
        return self._client[self._database_name][self._collection_name]

    def _construct_event(self, event_values: dict):
        event_values.pop('_id')
        event = Event(**event_values)
        return event

    def create_event(self, external_id):
        event_values = self._get_collection().find_one({"external_id": external_id})
        return self._construct_event(event_values)
