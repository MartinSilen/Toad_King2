from abc import abstractmethod, ABC

from main.common.business.models.command_class import Command


class CommandDispatcher(ABC):

    @abstractmethod
    def pass_command(self, command: Command):
        pass