from abc import ABC


class ActiveUsers(ABC):

    def get_active_user(self, user_id):
        ...

    def set_active_user_value(self, user_id, value_name, new_value):
        ...

    def delete_active_user(self, user_id):
        ...
