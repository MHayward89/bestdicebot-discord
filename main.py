import discord
import os
from random import randint
from dotenv import load_dotenv

load_dotenv()

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
        if diceFaceCount == 1:
          rollValue = 1
        else: 
          rollValue = randint(1, diceFaceCount)
        totalRollValue += rollValue
        messageString += str(rollValue)
        if i != numberOfDice - 1:
          messageString += "+"
      messageString += ") = " + str(totalRollValue)

    if len(messageString) > 1500:
      messageString = "Too loooooooooooooooooooooong"

    await message.channel.send(messageString)

  if message.content.startswith('!bear'):
      xSize = randint(400,500)
      ySize = randint(400,500)
      placeBearUrl = "https://placebear.com/" + str(xSize) + "/" + str(ySize)
      await message.channel.send(placeBearUrl)

client.run(os.environ.get('TOKEN'))
