import threading

from main.common.abstracts.controllers import command_handler
from main.common.business.IOsystem.command_queue import CommandQueue
from main.common.business.IOsystem.response_dispatcher import ResponseDispatcher
from main.common.business.IOsystem.response_queue import ResponseQueue
from main.common.business.controllers import command_handlers
from main.common.business.controllers.command_processing import CommandProcessor, AdminCommandDispatcher, \
    UserCommandDispatcher, SystemCommandDispatcher
from main.common.business.game_engine.core_engine import CoreEngine
from main.common.business.services.location_service import LocationServiceImplementation
from main.common.business.services.reply_service import ReplyServiceImplementation
from main.common.business.services.user_service import UserServiceImplementation


class Application:

    def __init__(self):
        self.command_queue = CommandQueue()
        self.response_queue = ResponseQueue()
        self.user_service = UserServiceImplementation()
        self.location_service = LocationServiceImplementation()
        self.reply_service = ReplyServiceImplementation()
        self.admin_dispatcher = AdminCommandDispatcher()
        self.system_dispatcher = SystemCommandDispatcher()
        self.response_dispatcher = ResponseDispatcher(self.response_queue)
        self.game_engine = CoreEngine(location_service=self.location_service, user_service=self.user_service,
                                      reply_service=self.reply_service, response_dispatcher=self.response_dispatcher)

        self.handlers_list = command_handlers.user_handler_factory(game_engine=self.game_engine,
                                                                   user_service=self.user_service,
                                                                   location_service=self.location_service)
        self.user_dispatcher = UserCommandDispatcher(handlers_dict=self.handlers_list, user_service=self.user_service)
        self.command_processor = CommandProcessor(admin_dispatcher=self.admin_dispatcher, user_dispatcher=self.user_dispatcher,
                                                  system_dispatcher=self.system_dispatcher)

    def process_command(self):
        while True:
            if self.command_queue.not_empty:
                self.command_processor.process_command(self.command_queue.get_command())


    def run_input_thread(self):
        thread = threading.Thread(target=self.process_command, daemon=True)
        print('input thread created')
        thread.run()
        print('app input started')




