from telegram import Update
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import ContextTypes
from telegram.ext import ApplicationBuilder
from telegram.ext import filters
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
import logging
import time


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level= logging.INFO
)

#Coded by H_SarrAllah

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.message.from_user.first_name
    keyboard = [
        [InlineKeyboardButton('اطلاعات کاربری', callback_data= 'info_fa')],
        [InlineKeyboardButton('Information User', callback_data= 'info_en')],
        [InlineKeyboardButton('Информация о пользователе', callback_data= 'info_ru')]
    ]
    
    await update.message.reply_text(
        text= f"Welcome❤️ '{name}'!\nThis robot was created by Ali Vaziri⌨️🤖\n\n🌐Option:\n💯'This robot is a simple robot to understand the user's user information'\n\nFor more information, you can send your question or request to the email below🥳.\n\nEmail: official.Vaziri@gmail.com\nID: @as_a_phenomenon\nmore bot: @Official_vaziri_bot",
        reply_markup= InlineKeyboardMarkup(keyboard)
    )

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await context.bot.send_message(chat_id= update.effective_chat.id, text= text)

async def Info(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    date = query.data
    
    
    if date == 'info_fa':
        photo = await context.bot.get_user_profile_photos(user_id= update.effective_chat.id)
        couch_prof = photo.total_count
        file = photo.photos[0][1].file_id
        name = update._effective_user.first_name
        username = update._effective_user.username
        number_id = update._effective_chat.id
        data = update._effective_message.date
        pm = f'اطلاعات کاربر😎:\n\n\n💟نام : {name}\n🗓نام کاربری : @{username}\n🎯ایدی عددی : {number_id}\n⚙️تاریخ ساخت : {data}\n⚖️تعداد پروفایل : {couch_prof}'
        await context.bot.send_photo(chat_id= update.effective_chat.id, photo=file, caption= pm)
        
    elif date == 'info_en':
        photo = await context.bot.get_user_profile_photos(user_id= update.effective_chat.id)
        couch_prof = photo.total_count
        file = photo.photos[0][1].file_id
        name = update._effective_user.first_name
        username = update._effective_user.username
        number_id = update._effective_chat.id
        data = update._effective_message.date
        pm = f'Information User😎:\n\n\n💟name : {name}\n🗓username : @{username}\n🎯number id : {number_id}\n⚙️Date acount : {data}\n⚖️count profile : {couch_prof}'
        
        await context.bot.send_photo(chat_id= update.effective_chat.id, photo=file, caption= pm)

    elif date == 'info_ru':
        photo = await context.bot.get_user_profile_photos(user_id= update.effective_chat.id)
        couch_prof = photo.total_count
        file = photo.photos[0][1].file_id
        name = update._effective_user.first_name
        username = update._effective_user.username
        number_id = update._effective_chat.id
        data = update._effective_message.date
        pm = f'Информация о пользователе😎:\n\n\n💟имя : {name}\n🗓имя пользователя : @{username}\n🎯идентификатор номера : {number_id}\n⚙️дата счета : {data}\n⚖️профиль подсчета : {couch_prof}'
    
        await context.bot.send_photo(chat_id= update.effective_chat.id, photo=file, caption= pm)

    
        
if __name__ == '__main__':
    Token = ApplicationBuilder().token("TOKEN").build()
    
    
    start_command = CommandHandler('start', start)
    echo_command = MessageHandler(filters.TEXT&(~filters.COMMAND), echo)
    start_handler = CallbackQueryHandler(Info)
 
 
 
    Token.add_handler(echo_command)
    Token.add_handler(start_command)
    Token.add_handler(start_handler)
    
    Token.run_polling()
    
    
    
    
