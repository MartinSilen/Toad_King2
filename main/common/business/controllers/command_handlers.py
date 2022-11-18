from main.common.abstracts.controllers.command_handler import CommandHandler
from main.common.business.IOsystem.response_dispatcher import ResponseDispatcher
from main.common.business.game_engine.core_engine import CoreEngine
from main.common.business.models.command_class import Command
from main.common.business.services.location_service import LocationServiceImplementation
from main.common.business.services.reply_service import ReplyServiceImplementation
from main.common.business.services.user_service import UserServiceImplementation
from main.common.external.models.location import Location
from main.common.external.models.user import User


class BaseUserHandler(CommandHandler):

    def __init__(self, user_service: UserServiceImplementation,
                 location_service: LocationServiceImplementation,
                 game_engine: CoreEngine):
        self.handler_name = 'base_user_handler'
        self.user_service = user_service
        self.location_service = location_service
        self.game_engine = game_engine
        self.command_list = {}
        self.current_user: User
        self.current_command: str
        self.current_command_args: list

    def _unpack_command(self, command: Command):
        self.current_user = self.user_service.get_user(command.user_id)
        self.current_command = command.command
        self.current_command_args = command.command_arguments

    def _move_user(self):
        self.game_engine.move_to_location(self.current_user, self.current_command_args[0])

    def _display_user_info(self):
        self.game_engine.display_character_info(self.current_user)

    def _respond_to_invalid_command(self):
        self.game_engine.invalid_command_response(self.current_user)

    def handle_command(self, command: Command):
        self._unpack_command(command)
        match self.current_command:
            case 'move':
                self._move_user()
            case 'character_info':
                self._display_user_info()
            case _:
                self._respond_to_invalid_command()


def user_handler_factory(user_service: UserServiceImplementation, location_service: LocationServiceImplementation,
                         game_engine: CoreEngine):
    user_handlers_list = {}
    base_handler = BaseUserHandler(user_service=user_service, location_service=location_service,
                                   game_engine=game_engine)
    user_handlers_list[base_handler.handler_name] = base_handler
    return user_handlers_list
