from .message_pattern import MessagePattern
import asyncio

"""
must have:

message_handler = MessageHandler(message_pattern, handler_function)

message_handler.matches(message)
message_handler.run_handler(context, message)

"""

class MessageHandler:
    def __init__(self, message_pattern, handler_function):
        self.message_pattern = MessagePattern(message_pattern)
        self.handler_function = handler_function


    def matches(self, message):
        '''
        returns True if the content of the message matches the message pattern
        otherwise returns False
        '''
        return self.message_pattern.get_match(message.content) is not None


    async def run_handler(self, context, message):
        '''
        runs the user defined handler according to the arguments
        of the message that match the pattern
        '''
        match_args = self.message_pattern.get_match(message.content)
        await self.handler_function(context, message, **match_args)

