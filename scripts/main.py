# imports
import discord
from settings import TOKEN, PREFIX
from handlers.message_handler_container import MessageHandlerContainer

message_handlers = MessageHandlerContainer(prefix=PREFIX)

@message_handlers.create_handler('say <string:msg>(.*)')
async def talk(context, user_message, msg):
    await user_message.delete()
    await user_message.channel.send(msg)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        await message_handlers.run_handlers(self, message)


client = MyClient()
client.run(TOKEN)

