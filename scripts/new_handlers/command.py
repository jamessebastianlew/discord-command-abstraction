from command_pattern import CommandPattern

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
        return self.command_pattern.matches(message.content)


    async def run_handler(self, context, message):
        pattern_args = self.command_pattern.get_args(message.content)
        await self.handler_function(context, message, **pattern_args)









