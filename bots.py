import telebot
import requests
from telebot import types

token="5311903541:AAHY9UCy_uBn2wzOilarHmjJiHAVcchIX3M"
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def welcome(message):


    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("IT ресурсы")
    item2 = types.KeyboardButton("Изучение Программирования")
    item3 = types.KeyboardButton("Релакс")
    item4 = types.KeyboardButton("APOD")
    item5 = types.KeyboardButton("Закрыть")


    markup.add(item1, item2, item3, item4,item5)

    bot.send_message(message.chat.id, "Привет! \nЯ - <b>{1.first_name}</b>, бот.".format(message.from_user, bot.get_me()),
    	parse_mode='html', reply_markup=markup)
name = '';
surname = '';
age = 0;
apod = '';
apodtext = '';
apodru = '';

@bot.message_handler(content_types=['text'])
def onetwothree(message):
	if message.chat.type == 'private':
		if message.text == 'Покажи IT ресурсы':
			bot.send_message(message.chat.id, "habrahabr.ru - Информационный ресурс, ориентированный на самую широкую аудиторию IT — от новичка до профессионала.\ncomnews.ru - Эжедневная газета в сфере IT\nappleinsider.ru - Объемный интернет ресурс для владельцев техники Apple\nferra.ru - российский журнал о потребительской электронике.")
		elif message.text == 'Изучение Программирования':
			bot.send_message(message.chat.id, "ru.bitdegree.org - Сайт, предлагающий массу бесплатных курсов, которые варьируются от программирования до разработки игр.\nwww.coursera.org - Coursera предоставляет курсы, учебные пособия и ресурсы по программированию от преподавателей ведущих университетов. На выбор вы найдёте сотни различных курсов, связанных с разработкой.\nwww.codecademy.com - один из самых популярных сайтов, где люди учатся программировать бесплатнo.\nwww.edx.org - массовая платформа с открытым исходным кодом для получения высшего образования.\nwww.codewars.com - Научит вас интересующему языку программирования с помощью комплекса задач для решения. Эти связанные с написанием кода задачи организованы по типу боевых искусств, каждая задача называется ката.")
		elif message.text == 'Релакс':
			bot.send_message(message.chat.id, "www.calm.com - Этот ресурс позволяет ненадолго отвлечься под спокойную музыку или во время расслабляющей медитации\nweavesilk.com - От движения вашей мышки на нем появляются линии, приобретающие необычную изломанную форму, как будто струящийся дым или туман.\nrainfor.me - Этот сайт позволит вам просто посидеть в тишине под звуки грозы. Здесь очень простой интерфейс и нет никаких отвлекающих визуальных элементов. Только шум дождя.\ntonematrix.audiotool.com - На экране вы увидите сетку небольших квадратов. Кликнув на квадрат, вы услышите отдельный звук. Нажимая квадраты по горизонтали, вы можете менять ритм, а по горизонтали – дополнять звуки.")
		elif message.text == "APOD":
			response = requests.get("https://api.nasa.gov/planetary/apod?api_key=AVqwbKdbgZo8e3gCrlhJKOc2a3303sh5lDEYdDLs")
			apod = response.json()["url"]
			apodtext = response.json()["explanation"]
			bot.send_message(message.chat.id, apod)
			bot.send_message(message.chat.id, apodtext)
		elif message.text == 'Закрыть':
			markup = types.ReplyKeyboardRemove(selective=False)
			bot.send_message(message.chat.id, 'sdelano', reply_markup=markup)
		elif message.text == 'Открыть':
			markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
			bot.send_message(message.chat.id, 'sdelano', reply_markup=markup)
		elif message.text == 'Привет':
			bot.send_message(message.from_user.id, "Как тебя зовут?");
			bot.register_next_step_handler(message, get_name);
def get_name(message):
	global name;
	name = message.text;
	bot.send_message(message.from_user.id, 'Привет, '+name+'. Какая у тебя фамилия?');
	bot.register_next_step_handler(message, get_surname);
def get_surname(message):
	global surname;
	surname = message.text;
	bot.send_message(message.from_user.id,'А сколько тебе лет то?');
	bot.register_next_step_handler(message, get_age);
def get_age(message):
	global age;
	while age == 0: #проверяем что возраст изменился
		age = int(message.text) #проверяем, что возраст введен корректно
	bot.send_message(message.from_user.id, 'Понял, '+name+', тебе ' +str(age)+' лет.')
@bot.message_handler(content_types=['voice'])
def onetwothreefour(message):
  if message.content_type == 'voice':
    bot.send_message(message.chat.id, "Голосовые не принимаю)")
bot.polling(none_stop=True)