from .message_handler import MessageHandler

"""

goal: use regex to make patternised messages

=========

i.e.

message_handler = MessageHandler(prefix=PREFIX)

@message_handler.create_handler(r'word <var_type:var_name>(pattern)')
async def function_name(context, message, var_name):
    pass

class Client(discord.Client):
    ...
    async def on_messsage(self, message):
        await message_handler.run_handlers(context, message)

=========

`context` represents the client object
`message` represents the discord.Message object
`var_name` is specified in the pattern

patterns will only match `expression` iff
pattern.fullmatch(expression)

"""


class MessageHandlerContainer:
    def __init__(self, prefix=''):
        self.handlers = []
        self.prefix = prefix

    
    def preprocess_pattern(self, message_pattern):
        '''
        adds prefix literal to the message pattern
        and reurns it adjusted message pattern
        '''
        return self.prefix + message_pattern

    def create_handler(self, message_pattern):
        '''
        returns a decorator function which creates a handler and adds it
        to the self.handlers for later processing
        '''
        message_pattern = self.preprocess_pattern(message_pattern)
        def add_handler_decorator(handler_function):
            message_handler = MessageHandler(message_pattern, handler_function)
            self.handlers.append(message_handler)

            return handler_function
        
        return add_handler_decorator


    async def run_handlers(self, context, message):
        '''
        asynchronous function runs all handlers against a message
        '''
        # to not waste any computation time going through all the handlers
        if not message.content.startswith(self.prefix):
            return

        for message_handler in self.handlers:
            if message_handler.matches(message):
                await message_handler.run_handler(context, message)

