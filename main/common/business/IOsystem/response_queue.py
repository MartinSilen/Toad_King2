from queue import Queue


class ResponseQueue(Queue):

    def __init__(self):
        super().__init__(100)

    def get_response(self):
        response = self.get()
        return response

    def add_response(self, response):
        self.put(response, timeout=1)