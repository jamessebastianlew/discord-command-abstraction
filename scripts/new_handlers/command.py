"""
must have:

command_obj = Command(command_pattern, handler_function)

command_obj.matches(message)
command_obj.run_handler(context, message)

"""

class Command():
    def __init__(self, command_pattern, handler_function):
        self.command_pattern = 


    def matches(self, message):
        re.fullmatch(



