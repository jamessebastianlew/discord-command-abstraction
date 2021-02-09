"""
must have:

command_obj = Command(command_pattern, handler_function)

command_obj.matches(message)
command_obj.run_handler(context, message)

"""

class Command:
    def __init__(self, command_pattern, handler_function):
        self.command_pattern = CommandPattern(command_pattern)
        self.handler_function = handler_function


    def matches(self, message):
        content = self.message.content
        if self.command_pattern.matches(message.content):






