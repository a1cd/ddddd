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
async def on_raw_message_edit(payload):
  on_message(payload.data)
@client.event
async def on_message(message):
    #create a lower version of the message for checking things
    RfndMsg = message.content.lower()
    if message.author == client.user:
      return
    print(str(message.author), "said: ", message.content)
    if str(message.content) == "spam":
      if message.channel != client.get_channel(768203883004035092):
        async with message.channel.typing():
          time.sleep((random.random() * .6) + 1)
          await message.channel.send("ಠ_ಠ")
        time.sleep((random.random() * 1) + 1)
        async with message.channel.typing():
          time.sleep((random.random() * 2) + 1)
          await message.channel.send("you actually want me to spam")
        time.sleep((random.random() * 2) + 1)
        async with message.channel.typing():
          time.sleep((random.random() * 1.5) + 1)
          await message.channel.send("in THIS channel?")
        time.sleep((random.random() * .2) + .5)
        async with message.channel.typing():
          time.sleep((random.random() * .6) + 1)
          await message.channel.send("there is literally a dedicated channel for it")
        time.sleep((random.random() * .2) + .6)
        async with message.channel.typing():
          time.sleep((random.random() * .6) + .3)
          await message.channel.send("<#768203883004035092>")
      else:
        for i in range(10):
          spaces = ""
          for b in range(4-len(str(i))):
            spaces = spaces + " "
          await message.channel.send("Hello! " + spaces + str(i+1) + "/25")

    #gossip
    if not(message.mentions == []):
      if random.choice([1,1,1,1,1,2]) == 2:
        time.sleep((random.random() * 2) + 1)
        async with message.channel.typing():
          time.sleep((random.random() * .6) + 1)
          await message.channel.send("__*ahem*__")
        time.sleep((random.random() * 2) + 1)
        async with message.channel.typing():
          time.sleep((random.random() * .6) + 1)
          await message.channel.send("i see there is some gossip")
        time.sleep((random.random() * 2) + 1)
        async with message.channel.typing():
          time.sleep((random.random() * .6) + 1)
          await message.channel.send("care to share?")
          time.sleep((random.random() * .6) + 1)
          await message.channel.send("Please?")

    #python runner thing
    if (RfndMsg.startswith("python3\n") or RfndMsg.startswith("python3\n")):
      filteredContent = message.content[8:]
      try:
        #print the compiled code
        print("global deecodeded\ndef deecodeded():\n    " + filteredContent.replace("\n", "\n    ") + "\ndeecodeded()")
        compiledContent = compile("global deecodeded\ndef deecodeded():\n    " + filteredContent.replace("\n", "\n    ") + "\ndeecodeded()", "<string>", "exec")
        exec(compiledContent)
        codeResponse = deecodeded()
        print (codeResponse)
      except Exception as e:
        await message.channel.send("an error occored :/")
        codeResponse = e
      if (type(codeResponse) == type(None)):
        await message.channel.send("code did not return info")
      else:
        await message.channel.send("```python\n" + str(codeResponse) + "```")



client.run('NzcwNzM2OTgzOTkwNzMwNzYz.X5h6wA.FOip2X10gkx_OZapvzvsj7W3hYE')
