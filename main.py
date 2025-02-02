py -3 -m pip install -U discord.py


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('MTMzMjU5NzU1NzAxMTkzOTM4MA.GwSRfi.fRal6Kj5ERA1M58XNyQmC6SPhTZK_qLZBXp91s'))
