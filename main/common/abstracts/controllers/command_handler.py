from abc import ABC, abstractmethod

from main.common.business.models.command_class import Command


class CommandHandler(ABC):

    @abstractmethod
    def handle_command(self, command: Command):
        ...
