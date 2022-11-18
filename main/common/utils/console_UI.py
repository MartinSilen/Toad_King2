import re
import threading


from main.common.business.IOsystem.command_queue import CommandQueue
from main.common.business.IOsystem.response_queue import ResponseQueue
from main.common.business.models.command_class import Command


class ConsoleUI:

    def __init__(self, command_queue: CommandQueue, response_queue: ResponseQueue):
        self.command_queue = command_queue
        self.response_queue = response_queue

    def format_command_arguments(self, arguments=''):
        message = arguments.casefold()
        command_arguments = message.split()
        command_arguments.pop(0)
        return command_arguments

    def format_command(self, command):
        prepared_command = command.casefold()
        prepared_command = prepared_command.split()
        prepared_command = prepared_command[0]
        prepared_command = re.sub(r'\A/', '', prepared_command)
        return prepared_command

    def send_command(self, user_id, command, command_arguments):
        command = self.format_command(command)
        command_args = self.format_command_arguments(command_arguments)
        asembled_command = Command(user_id=user_id, command=command, command_arguments=command_args)
        self.command_queue.add_command(asembled_command)

    def read_command(self):
        while True:
            command_text = input('Enter Command: \n')
            self.send_command('1', command_text, command_text)

    def output_command(self):
        while True:
            if self.response_queue.not_empty:
                print(self.response_queue.get_response().message)

    def start_threads(self):
        input_thread = threading.Thread(target=self.read_command, daemon=True)
        output_thread = threading.Thread(target=self.output_command, daemon=True)
        input_thread.run()
        output_thread.run()
        print('io threads started')

