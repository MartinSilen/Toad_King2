from main.common.abstracts.IOsystem.response_dispatcher import ResponseDispatcherInterface
from main.common.business.IOsystem.response_queue import ResponseQueue
from main.common.business.models.response_class import Response


class ResponseDispatcher(ResponseDispatcherInterface):

    def __init__(self, response_queue: ResponseQueue):
        self.response_queue = response_queue

    def send_response(self, response: Response):
        self.response_queue.add_response(response)


