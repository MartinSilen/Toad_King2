import dataclasses
import os

from dotenv import load_dotenv
from pymongo import MongoClient

from main.common.external.models.game_object import GameObject
from main.common.external.models.location import Location



class DaoLocationImplementation:
    def __init__(self):
        load_dotenv()
        self._DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
        self._DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
        self._DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
        self._database_name = os.getenv('DATABASE_NAME')
        self._collection_name = 'locations'
        self._client = MongoClient(self._DATABASE_CONNECTION_STRING, document_class=dict)

    def _unpack_objects(self, objects_data):
        unpacked_objects = {}
        for object in objects_data:
            unpacked_objects[object['object_name']] = GameObject(**object)
        return unpacked_objects

    def _reconstruct_location(self, location_values: dict):
        location_values.pop('_id')
        location = Location(**location_values)
        location.objects = self._unpack_objects(location.objects)
        return location

    def _get_collection(self):
        return self._client[self._database_name][self._collection_name]

    def find_by_id(self, external_id):
        location = self._get_collection().find_one({"external_id": external_id})
        return self._reconstruct_location(location)

    def insert(self, location: Location):
        return self._get_collection().insert_one(dataclasses.asdict(location))

    def update(self, location: Location):
        return self._get_collection().update_one({"external_id": location.external_id}, {'$set': dataclasses.asdict(location)})

    def delete_by_id(self, external_id: str):
        return self._get_collection().delete_one({"external_id": external_id})


