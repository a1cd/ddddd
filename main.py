import discord, time, random

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #for i in range(25):
    #  spaces = ""
    #  for b in range(4-len(str(i))):
    #    spaces = spaces + " "
    #  await client.get_channel(768203883004035092).send("Hello! " + spaces + str(i+1) + "/25")
    #await client.get_channel(768203883004035092).send("Finished Saying 'Hello' 25 times! ur welcome :)")


@client.event
async def on_message(message):
    if str(message.content) == "p.ping":
      await message.channel.send("ಠ_ಠ")
    print(message)
client.run('NzcwNzM2OTgzOTkwNzMwNzYz.X5h6wA.FOip2X10gkx_OZapvzvsj7W3hYE')