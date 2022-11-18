import dataclasses
import os

from dotenv import load_dotenv
from pymongo import MongoClient

from main.common.external.models.reply import Reply


class DaoReplyImplementation:

    def __init__(self):
        load_dotenv()
        self._DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
        self._DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
        self._DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
        self._database_name = os.getenv('DATABASE_NAME')
        self._collection_name = 'replies'
        self._client = MongoClient(self._DATABASE_CONNECTION_STRING, document_class=dict)

    def _get_collection(self):
        return self._client[self._database_name][self._collection_name]

    def find_by_id(self, external_id) -> str:
        reply = self._get_collection().find_one({"external_id": external_id})
        if reply is not None:
            return reply['contents']
        else:
            return 'Reply not here yet!'

    def insert(self, reply: Reply):
        return self._get_collection().insert_one(dataclasses.asdict(reply))

