import dataclasses
import os

from dotenv import load_dotenv
from pymongo import MongoClient

from main.common.external.models.event import Event


class DaoEventImplementation:

    def __init__(self):
        load_dotenv()
        self._DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
        self._DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
        self._DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
        self._database_name = os.getenv('DATABASE_NAME')
        self._collection_name = 'events'
        self._client = MongoClient(self._DATABASE_CONNECTION_STRING, document_class=dict)

    def _reconstruct_event(self, event_values: dict):
        event_values.pop('_id')
        event = Event(**event_values)
        return event

    def _get_collection(self):
        return self._client[self._database_name][self._collection_name]

    def get_by_id(self, external_id):
        event_data = self._get_collection().find_one({"external_id": external_id})
        return self._reconstruct_event(event_data)

    def insert(self, event: Event):
        return self._get_collection().insert_one(dataclasses.asdict(event))

    def update(self, event: Event):
        return self._get_collection().update_one({"external_id": event.external_id}, {'$set': dataclasses.asdict(event)})
