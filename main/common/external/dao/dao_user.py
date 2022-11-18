import dataclasses
import os
from contextlib import contextmanager
from typing import Type

from dotenv import load_dotenv
from pymongo import MongoClient

from main.common.external.models.active_ability import ActiveAbility
from main.common.external.models.user import User


class DaoUserImplementation:
    def __init__(self):
        load_dotenv()
        self._DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
        self._DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
        self._DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
        self._database_name = os.getenv('DATABASE_NAME')
        self._collection_name = 'users'
        self._client = MongoClient(self._DATABASE_CONNECTION_STRING, document_class=dict)

    def _unpack_abilities(self, abilities: dict):
        unpacked_abilities = {}
        if abilities is not None:
            for ability in abilities:
                unpacked_abilities[ability['ability_name']] = ActiveAbility(**ability)
        return unpacked_abilities

    def _reconstruct_user(self, user_values: dict):
        if user_values is not None:
            user_values.pop('_id')
            user = User(**user_values)
            user.character_active_abilities = self._unpack_abilities(user.character_active_abilities)
            return user
        else:
            return None

    def _get_collection(self):
        return self._client[self._database_name][self._collection_name]

    def find_by_id(self, external_id):
        user = self._get_collection().find_one({"external_id": external_id})
        return self._reconstruct_user(user)

    def find_by_character_name(self, name):
        user = self._get_collection().find_one({"character_name": name})
        return self._reconstruct_user(user)

    def insert(self, user: User):
        return self._get_collection().insert_one(dataclasses.asdict(user))

    def update(self, user: User):
        return self._get_collection().update_one({"external_id": user.external_id}, {'$set': dataclasses.asdict(user)})

    def delete_by_id(self, external_id: str):
        return self._get_collection().delete_one({"external_id": external_id})


