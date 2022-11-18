from queue import Queue


class CommandQueue(Queue):

    def __init__(self):
        super().__init__(100)

    def get_command(self):
        response = self.get()
        return response

    def add_command(self, command):
        self.put(command, timeout=1)