from main.common.external.models.user import User


class ActiveUserDict:

    def __init__(self):
        self.storage = {}

    def add_active_user(self, user: User):
        self.storage[user.external_id] = user

    def get_active_user(self, user_id):
        return self.storage[user_id]

    def update_active_user(self, user_id, user: User):
        self.storage[user_id] = user

    def delete_active_user(self, user_id):
        self.storage.pop(user_id)