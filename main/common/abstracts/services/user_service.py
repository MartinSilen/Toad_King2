from abc import ABC

from main.common.external.models.user import User


class AbstractUserService(ABC):

    def create_new_user(self, user_id, kwargs=None):
        ...

    def get_user(self, user_id):
        ...

    def update_user(self, user: User):
        ...

    def delete_user(self, user_id):
        ...

