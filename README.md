# The Discord Bot Command Abstraction API for Python

A main part of many Discord bots is communicating with the bot via commands in Discord channels.

This API aims to ease the process of creating easily extendable and maintainable commands through an abstraction.

## Current API Features

- Message handler - the main feature of the Discord Command Abstraction APIis to have an easy way to recognise messages that are meant for your bot. This is done through our MessageHandler class (examples below)
- Capable of creating multiple message handlers (meaning you can seperate message handlers into seperate files) and seperate logic into easy to read and easy to maintain modules of code.

example main.py file:
```py
from settings import TOKEN, PREFIX
from handlers.message_handler import MessageHandler
import discord

# create as many message handlers as you want!
# we are creating just one
message_handler = MessageHandler()


# the pattern 'say <string:var_name>' will respond to
# patterns that match 'say' followed by a string word
# the `string` in <string:var_name> is the type that
# the argument will be converted to and the `var_name`
# in <string:var_name> is the argument that will be
# passed into your function

# this message handler will respond to messages like
# 'say hello"
# 'say 123"

@message_handler.create_handler('say <string:var_name>')
async def say_handler(user_message, var_name):
    await user_message.delete()
    await user_message.channel.send(msg)

# notice that arguments `a` and `b` are translated into integers
@message_handler.create_handler('multiply <int:a> <int:b>')
async def multiply_handler(user_message, a, b):
    await user_message.channel.send(str(a * b))


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.content.startswith(PREFIX):
            return

        arguments = message.content[len(PREFIX):].split()
        
        # all you need to do to run the handlers is to
        # await this function with the arguments in the message
        # it will automatically check to see if any commands match
        await message_handler.run_handlers(message, arguments)

client = MyClient()
client.run(TOKEN)
```

## The upcoming API

In order to make this API even more versatile, we have decided to add advanced pattern (to recognise discord commands from the chat) matching using regex!

Commands such as 'say \<string:var\_name\>([abc]+)' for example, will match any command tat comprises of "say " followed by a word only containing letters a, b, or c.

Features:
- regex pattern matching
- type conversion
- builtin prefix checking

example use:
```py
from settings import TOKEN, PREFIX
from handlers.message_handler import MessageHandler
import discord

# create as many message handlers as you want!
# we are creating just one
command_handler = CommandHandler(prefix=PREFIX)


# format for variable arguments is as so:
# <var_type:var_name>(regex pattern)
@command_handler.create_handler(r'printword <string:var_name>(\w+)')
async def say_handler(context, user_message, var_name):
    # `context` represents the discord client
    # `user_message` represents the message object (from discord.py API)
    await user_message.channel.send(var_name)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # this is the only line you need to run the handlers
        await message_handler.run_handlers(self, message)

client = MyClient()
client.run(TOKEN)
```
