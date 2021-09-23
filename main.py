import sys
from telebot import *
import telebot
from bs4 import BeautifulSoup
import requests as req
from selenium import webdriver
from interface import *
import pandas as pd

from datetime import time, datetime

import requests
import logging
import time
# Импорт класса для работы с потоками
from PyQt5.QtCore import QThread, pyqtSignal
# Импорт сигналов для связи между потоками
from PyQt5.QtWidgets import QSystemTrayIcon, QStyle, QAction, qApp, QMenu
# BOT_TOKEN = '1755676306:AAHKqhFE0h-HWx1vuJewNrqypplPUcpG3Sk'
BOT_TOKEN = '1955330750:AAFfJo1gaeeIH0M_iizRPMtCCbnqDi4vY6U'
CHANEL_NAME = "@investinfor"
client = telebot.TeleBot(BOT_TOKEN)

path = "https://finviz.com/map.ashx?t=sec"


@client.message_handler(commands=['start'])
def get_commands(message):
    # redline = types.ReplyKeyboardMarkup(resize_keyboard=True) # Тип кнопок выводящихся снизу канала
    markup_inline = types.InlineKeyboardMarkup()  # Тип кнопок выводящихся под сообщением
    # button_id = types.InlineKeyboardButton(text='Просканить канал 📻', callback_data='channel')
    sp500 = types.InlineKeyboardButton(text='S&P500', callback_data='sp500')
    activ = types.InlineKeyboardButton(text='Активные акции', callback_data='activinvest')
    # redline.row("Просканировать канал", "Найти музыку")
    markup_inline.add(activ)
    if message.text == "/start":
        client.send_message(message.chat.id, "Привет, я бот и вот что я могу:", reply_markup=markup_inline)

@client.callback_query_handler(func=lambda call: True)
def answer(call):
    # if call.data == "sp500":
    #     driver = webdriver.Chrome()
    #     driver.get(path)
    #     a = driver.find_element_by_xpath(
    #         '/html/body/div[2]/div/div[3]/div/div[1]/div/div[1]/canvas[2]').screenshot_as_png
    #     driver.close()
    #     # resp = req.get(path)
    #     # soup = BeautifulSoup(resp.text, 'lxml')
    #     # a = soup.find_all("canvas", class_="hover-canvas")
    #     client.send_photo(call.message.chat.id, a)

    if call.data == "activinvest":
        resp = req.get("https://finance.yahoo.com/most-active")
        soup = BeautifulSoup(resp.text, 'lxml')
        web_frames = pd.read_html(soup.prettify())
        web_frames = web_frames[0].iloc[0:25, 0:9]
        web_frames.to_excel("cryptocoins.xlsx")
        with open("cryptocoins.xlsx", 'rb') as file:
            fileread = file.read()
            client.send_document(call.message.chat.id, fileread, caption="excel")

client.polling()



