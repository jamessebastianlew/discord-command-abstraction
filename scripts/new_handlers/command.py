from .command_pattern import CommandPattern
import asyncio

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
        '''
        returns True if the content of the message matches the command pattern
        otherwise returns False
        '''
        return self.command_pattern.get_match(message.content) is not None


    async def run_handler(self, context, message):
        '''
        runs the user defined handler according to the arguments
        of the message that match the pattern
        '''
        match_args = self.command_pattern.get_match(message.content)
        await self.handler_function(context, message, **match_args)
