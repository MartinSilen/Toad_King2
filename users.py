import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass

from commandhandlers import CommandHandlerInterface

from gamedatabase import DatabaseInterface


class UserManagerInterface(ABC):

    @abstractmethod
    def get_user_info(self, user_id, field=None):
        pass

    @abstractmethod
    def modify_user_info(self, user_id, value, new_value):
        pass

    @abstractmethod
    def deactivate_user(self, user_id):
        pass

    @abstractmethod
    def save_active_users(self):
        pass

    @abstractmethod
    def pass_command_to_handler(self, user_id, command, command_args=None):
        pass


@dataclass
class ActiveAbility:
    ability_name: str
    cooldown: int = 0


@dataclass
class ActiveUser:
    identifier: int
    user_info: dict
    character_name: str
    character_active_abilities: [ActiveAbility] = None
    command_handler: CommandHandlerInterface = None
    inactivity_counter: int = 0



class UserManager(UserManagerInterface):

    def __init__(self, user_database: DatabaseInterface):
        self.active_users = {}
        self.user_database = user_database
        self.lock = threading.Lock()

    def add_new_user(self, user_id):
        self.user_database.add_line(user_id)
        self.user_database.modify_value(user_id, 'command_handler', 'new_user_handler')
        self.user_database.save_database()

    def create_active_user(self, user_id):
        if self.user_database.index_exists(user_id):
            user_info = self.user_database.get_line_as_dict(user_id)
            with self.lock:
                new_active_user = ActiveUser(user_info)
                self.active_users[user_id] = new_active_user
        else:
            self.add_new_user(user_id)
            self.create_active_user(user_id)

    def is_in_active_users(self, user_id):
        if user_id in self.active_users:
            return True
        else:
            return False

    def ensure_user_initialization(self, user_id):
        if not self.is_in_active_users(user_id):
            self.create_active_user(user_id)

    def get_user_info(self, user_id, field=None):
        self.ensure_user_initialization(user_id)
        with self.lock:
            if field is not None:
                return self.active_users[user_id].user_info[field]
            else:
                return self.active_users[user_id].user_info

    def modify_user_info(self, user_id, value, new_value):
        self.ensure_user_initialization(user_id)
        with self.lock:
            if isinstance(self.active_users[user_id].user_info[value], new_value.__class__):
                self.active_users[user_id].user_info[value] = new_value
            else:
                raise TypeError

    def save_active_user(self, user_id):
        with self.lock:
            for value in self.active_users[user_id].user_info:
                self.user_database.modify_value(user_id, value, self.active_users[user_id].user_info[value])

    def deactivate_user(self, user_id):
        self.save_active_user(user_id)
        with self.lock:
            self.active_users.pop(user_id)

    def save_active_users(self):
        for user in self.active_users:
            self.save_active_user(user)

    def pass_command_to_handler(self, user_id, command, command_args=None):
        self.ensure_user_initialization(user_id)
        self.active_users[user_id].command_handler.handle_command(command, command_args)


