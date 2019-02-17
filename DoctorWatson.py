from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('DoctorWatson') #creating instance
bot.set_trainer(ListTrainer)

for files in os.listdir('C:/Users/User/Desktop/ProjectModule/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
 data = open('C:/Users/User/Desktop/ProjectModule/chatterbot-corpus-master/chatterbot_corpus/data/english/' + files, 'r').readlines()
 bot.train(data)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
	
while True:
	message = input('User:')
	if message.strip() != 'Bye':
		reply = bot.get_response(message)
		print('Doctor Watson : ',reply)
	if message.strip() == 'Bye': 
		print('Doctor Watson : Bye')
		break