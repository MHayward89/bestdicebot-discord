import discord
import os
from random import randrange

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/r'):
    messageString = "Nah mate"
    splitMessage = message.content.split()
    diceRoll = splitMessage[1].split('d')
    try:
      numberOfDice = int(diceRoll[0])
      diceFaceCount = int(diceRoll[1])
    except:
      numberOfDice = 0
      diceFaceCount = 0
      messageString = "Try numbers idiot"

    totalRollValue = 0

    if numberOfDice > 0 and numberOfDice <= 1000 and diceFaceCount > 0 and diceFaceCount <= 10000:
      messageString = splitMessage[1] + " = ("
      for i in range(0, numberOfDice):
        rollValue = randrange(0, diceFaceCount)
        totalRollValue += rollValue
        messageString += str(rollValue)
        if (i != numberOfDice - 1):
          messageString += "+"
      messageString += ") = " + str(totalRollValue)

    if len(messageString) > 1500:
      messageString = "Too loooooooooooooooooooooong"

    await message.channel.send(messageString)

client.run(os.getenv('TOKEN'))
