import discord
import asyncio
import os
from trigger import Trigger

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

good_shit = "👌👀👌👀👌👀👌👀👌👀 good shit go౦ԁ sHit👌 thats ✔ some good👌👌shit right👌👌there👌👌👌 right✔there ✔✔if i do ƽaү so my self 💯 i say so 💯 thats what im talking about right there right there (chorus: ʳᶦᵍʰᵗ ᵗʰᵉʳᵉ) mMMMMᎷМ💯 👌👌 👌НO0ОଠOOOOOОଠଠOoooᵒᵒᵒᵒᵒᵒᵒᵒᵒ👌 👌👌 👌 💯 👌 👀 👀 👀 👌👌Good shit "

triggers = [Trigger('goOd sHit', good_shit),
            Trigger('kek', ':pineapple:')]

@client.event
async def on_message(message):
    for trigger in triggers:
        if trigger.is_triggered(message):
            await client.send_message(message.channel,
                                      trigger.output(message))

client.run(os.environ['discord_user'], os.environ['discord_pass'])
