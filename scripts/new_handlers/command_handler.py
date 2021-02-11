from .command import Command

"""

goal: use regex to make patternised commands

=========

i.e.

message_handler = CommandHandler(prefix=PREFIX)

@message_handler.create_handler(r'word <var_type:var_name>(pattern)')
async def function_name(context, message, var_name):
    pass

class Client(discord.Client):
    ...
    async def on_messsage(self, message):
        await message_handler.run_handlers(context, message)

=========

`context` represents the client object
`message` represents the message
`var_name` is specified in the pattern

patterns will only match `expression` iff
pattern.fullmatch(expression)

"""


class CommandHandler:
    def __init__(self, prefix=''):
        self.handlers = []
        self.prefix = prefix

    
    def preprocess_pattern(self, command_pattern):
        '''
        adds prefix literal to the command pattern
        and reurns it adjusted command pattern
        '''
        return self.prefix + command_pattern

    def create_handler(self, command_pattern):
        '''
        returns a decorator function which creates a handler and adds it
        to the self.handlers for later processing
        '''
        command_pattern = self.preprocess_pattern(command_pattern)
        def add_handler_decorator(handler_function):
            command = Command(command_pattern, handler_function)
            self.handlers.append(command)

            return handler_function
        
        return add_handler_decorator


    async def run_handlers(self, context, message):
        '''
        asynchronous function runs all handlers against a message
        '''
        for command in self.handlers:
            if command.matches(message):
                await command.run_handler(context, message)

