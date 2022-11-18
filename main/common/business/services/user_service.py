import dataclasses
import threading

from main.common.abstracts.services.user_service import AbstractUserService
from main.common.external.dao.dao_user import DaoUserImplementation
from main.common.external.models.user import User


class UserServiceImplementation(AbstractUserService):
    _DAO_USER = DaoUserImplementation()
    lock = threading.Lock()

    def create_new_user(self, user_id, kwargs=None):
        if kwargs is None:
            user = User(external_id=user_id, character_name='JohnDoe')
        else:
            user = User(external_id=user_id, **kwargs)
        with self.lock:
            self._DAO_USER.insert(user)

    def get_user(self, user_id):
        with self.lock:
            found_user = self._DAO_USER.find_by_id(user_id)
        if found_user is None:
            self.create_new_user(user_id)
            self.get_user(user_id)
        return found_user


    def update_user(self, user):
        with self.lock:
            self._DAO_USER.update(user)

    def delete_user(self, user_id):
        with self.lock:
            self._DAO_USER.delete_by_id(user_id)








