import telebot # Importamos las librería

TOKEN = '2016049085:AAHLf-t0nqMtCgQYw6dnoI4w-7J0qGajgrk' # Ponemos nuestro Token generado con el @BotFather

tb = telebot.TeleBot(TOKEN)


def mensaje(mensaje):
    tb.send_message('-546149888', mensaje)
