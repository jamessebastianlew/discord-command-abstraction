# The Discord Bot Command Abstraction API for Python

A main part of many Discord bots is communicating with the bot via commands in Discord channels.

This API aims to ease the process of creating easily extendable and maintainable commands through an abstraction.

This repo contains two main projects:
- an advanced message pattern matching API (The Default API)
- a simple message pattern matching API (Simple Handler API)

## The Default API

In order to make this API even more versatile, we have decided to add advanced pattern matching using regex (to recognise discord messages which match the pattern)!

Message patterns such as `say <string:var_name>([abc]+)`, for example, will match any command that comprises of "say " followed by a word only containing letters a, b or c and pass that word (converted to string) to your handler function.

NOTE: a 'handler' refers to a function which handles the bots processing of a message

Features:
- regex pattern matching
- type conversion
- builtin prefix checking
- simple and easy to use
- modular - easy to detach from your bot and seperate into files
- make as many handlers and handler containers as you want!

example use:
```py
import discord
from settings import TOKEN, PREFIX

# import the message handler container
from handlers.message_handler_container import MessageHandlerContainer

# make an instance
# this container will hold all your message handler functions
# and is able to process all the handlers in one go!
message_handlers = MessageHandlerContainer(prefix=PREFIX)

# create a handler function for a pattern using the .create_handler function!
# the variables will be automatically passed to your function as arguments!
#   e.g. the `msg` variable below which is in the pattern
# the first two arguments `context` and `user_message` are the arguments
# you pass to message_handlers.run_handlers!
@message_handlers.create_handler('say <string:msg>(.*)')
async def talk(context, user_message, msg):
    await user_message.delete()
    await user_message.channel.send(msg)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # simply asynchronously await all running all the handlers you've made!
        # NOTE: these two arguments will be passed to your handler function
        #       as the first two arguments! you can replace `self` with anything
        #       but `message` must be a discord.Message instance.
        #       this is so you can pass any necessary information that you need.
        await message_handlers.run_handlers(self, message)


client = MyClient()
client.run(TOKEN)
```

## Simple Handler API Features

This is the previous iteration of message handlers used a similar way of pattern matching except far simpler. Patterns consisted of literal (things that the user match exactly) and variable words (that can change based on use input) that MUST BE SPACE SEPERATED.

examples:

the pattern `'multiply <int:a> <int:b>'` will match messages such as `'multiply 123 2'` but not `'multiply  123 2'` (two spaces).
the pattern `'say <string:msg>'` will match messages such as `'say hello'` but not `'say hello hi'` 

example main file:
```py
import discord
from settings import TOKEN, PREFIX
from simple_handlers.message_handler_container import MessageHandlerContainer

message_handlers = MessageHandlerContainer(prefix=PREFIX)

# NOTE: the <string:msg> pattern will only match a SINGLE WORD
#       all variables are space seperated
@message_handlers.create_handler('say <string:msg>')
async def talk(user_message, msg):
    await user_message.channel.send(msg)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        await message_handlers.run_handlers(message)


client = MyClient()
client.run(TOKEN)
```

