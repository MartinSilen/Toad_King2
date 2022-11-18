from main.common.abstracts.controllers.command_dispatcher import CommandDispatcher
from main.common.abstracts.controllers.command_handler import CommandHandler
from main.common.business.controllers import command_handlers
from main.common.business.game_engine.core_engine import CoreEngine
from main.common.business.models.command_class import Command
from main.common.business.services.location_service import LocationServiceImplementation
from main.common.business.services.user_service import UserServiceImplementation


user_command_handlers_registry = {str: CommandHandler}


class MissingCommandHandler(Exception):
    pass


class IncorrectCommandType(Exception):
    pass


class CommandProcessor:

    def __init__(self, user_dispatcher: CommandDispatcher, admin_dispatcher: CommandDispatcher,
                 system_dispatcher: CommandDispatcher):
        self.user_dispatcher = user_dispatcher
        self.admin_dispatcher = admin_dispatcher
        self.system_dispatcher = system_dispatcher

    def process_command(self, command: Command):
        match command.command_type:
            case 'user':
                self.user_dispatcher.pass_command(command)
            case 'admin':
                self.admin_dispatcher.pass_command(command)
            case 'system':
                self.system_dispatcher.pass_command(command)
            case _:
                raise IncorrectCommandType


class UserCommandDispatcher(CommandDispatcher):

    def __init__(self, user_service: UserServiceImplementation, handlers_dict):
        self.user_service = user_service
        self.user_command_handlers_list = handlers_dict

    def pass_command(self, command: Command):
        user = self.user_service.get_user(command.user_id)
        try:
            if user.command_handler_name in self.user_command_handlers_list:
                self.user_command_handlers_list[user.command_handler_name].handle_command(command)
            else:
                raise MissingCommandHandler
        except MissingCommandHandler:
            print('handler name was: ' + user.command_handler_name)
            print('handlers list is ' + str(self.user_command_handlers_list))



class AdminCommandDispatcher(CommandDispatcher):

    def pass_command(self, command: Command):
        raise NotImplemented


class SystemCommandDispatcher(CommandDispatcher):

    def pass_command(self, command: Command):
        raise NotImplemented


def build_command_processor(user_service: UserServiceImplementation, location_service: LocationServiceImplementation,
                         game_engine: CoreEngine):
    command_processor = CommandProcessor(UserCommandDispatcher(user_service,
                                                               command_handlers.user_handler_factory(user_service,
                                                                                                     location_service,
                                                                                                     game_engine)),
                                         AdminCommandDispatcher(),
                                         SystemCommandDispatcher())
    return command_processor
