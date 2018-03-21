from chatterbot.trainers import ListTrainer #method to train the chatbot.
from chatterbot import ChatBot	#import the chatbot.
import os

bot = ChatBot('Test') #create the chatbot

bot.set_trainer(ListTrainer) #set the trainer

while True:
	request = input('You: ')
	response = bot.get_response(request)

	print('Bot: ', response)