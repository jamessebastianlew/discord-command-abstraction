'''
The following file contains a sample usage of the
Simple Discord Bot Command Handler API and it is
recommended that a user uses the newer regex-based
message handler API.
'''

import discord
from settings import TOKEN, PREFIX
from simple_handlers.message_handler_container import MessageHandlerContainer

message_handlers = MessageHandlerContainer(prefix=PREFIX)

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
