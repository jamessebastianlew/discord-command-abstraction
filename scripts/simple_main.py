# imports
from settings import TOKEN, PREFIX
from simple_handlers.command_handler import CommandHandler
import discord

command_handler = CommandHandler(prefix=PREFIX)

@command_handler.create_handler('say <string:msg>')
async def talk(user_message, msg):
    await user_message.channel.send(msg)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        await command_handler.run_handlers(message)


client = MyClient()
client.run(TOKEN)
