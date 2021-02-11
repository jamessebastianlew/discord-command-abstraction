import asyncio
from typing import List
from .message_pattern import MessagePattern

"""
message handler has three main functions

1. create a handler to a pattern (decorator)
2. run all handlers asynchronously if they match
"""

class MessageHandlerContainer:
    def __init__(self, prefix: str = ''):
        self.handlers = []
        self.prefix = prefix

    def create_handler(self, pattern: str):
        '''
        considers a pattern

        returns a decorator which adds the given function to
        list of handlers along with the pattern
        '''
        message_pattern = MessagePattern(pattern)

        def decorated_handler(pattern_handler):
            self.handlers.append((message_pattern, pattern_handler))
            return pattern_handler

        return decorated_handler

    async def run_handlers(self, message):
        '''
        runs all the handlers in self.handlers
        '''
        if not message.content.startswith(self.prefix):
            return

        stripped_message = message.content[len(self.prefix):]
        arguments = stripped_message.split()

        for message_pattern, pattern_handler in self.handlers:
            pattern_object = message_pattern.gen_object(arguments)

            if pattern_object is not None:
                await pattern_handler(message, **pattern_object)
