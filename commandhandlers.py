from abc import ABC, abstractmethod


class CommandHandlerInterface(ABC):

    @abstractmethod
    def handle_command(self, command, command_args):
        pass


class CommandHandler(CommandHandlerInterface):

    def __init__(self, user_id, user_manager, location_manager, event_manager, object_manager):
        self.user_manager = user_manager
        self.location_manager = location_manager
        self.event_manager = event_manager
        self.object_manager = object_manager
        self.user_id = user_id
        self.command_list = {'move': self.move}

    def handle_command(self, command, command_args):
        self.command_list[command](command_args)

    def move(self, target):
        pass


class LocationHandler(CommandHandler):

    def __init__(self, user_id, user_manager, location_manager, event_manager, object_manager):
        super().__init__(user_id, user_manager, location_manager, event_manager, object_manager)
        self.unique_commands = {}
        self.command_list = self.command_list | self.unique_commands



class EventHandler(CommandHandler):
    pass


class TemporaryHandler(CommandHandler):
    pass


class GreenvaleHandler(LocationHandler):

    def __init__(self, user_id, user_manager, location_manager, event_manager, object_manager):
        super().__init__(user_id, user_manager, location_manager, event_manager, object_manager)
        self.unique_commands = {}
        self.command_list = self.command_list | self.unique_commands




class CommandHandlerFactory:

    def __init__(self, user_manager, location_manager, event_manager, object_manager):
        self.user_manager = user_manager
        self.location_manager = location_manager
        self.event_manager = event_manager
        self.object_manager = object_manager
        self.handler_types = {'greenvale_handler': GreenvaleHandler}

    def create_handler(self, handler_name, user_id):
        return self.handler_types[handler_name](user_id, self.user_manager, self.location_manager, self.event_manager,
                                                self.object_manager)
