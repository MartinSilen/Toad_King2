from abc import ABC, abstractmethod
from main.common.business.models.response_class import Response


class ResponseDispatcherInterface(ABC):

    @abstractmethod
    def send_response(self, response: Response):
        ...
