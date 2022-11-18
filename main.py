import threading

from main.common.utils.application import Application
from main.common.utils.console_UI import ConsoleUI

if __name__ == '__main__':
    application = Application()
    print('app created')
    console_UI = ConsoleUI(application.command_queue, application.response_queue)
    print('ui created')
    app_input_thread = threading.Thread(target=application.process_command)
    UI_input_thread = threading.Thread(target=console_UI.read_command)
    UI_output_thread = threading.Thread(target=console_UI.output_command)
    print('Threads Created')
    app_input_thread.start()
    print('app thread started')
    UI_input_thread.start()
    print('input thread started')
    UI_output_thread.start()
    print('output thread started')



