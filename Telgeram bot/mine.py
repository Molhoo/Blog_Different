from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters , ContextTypes
from telegram.ext import ApplicationBuilder

TOKEN: Final = 'YOUR TOKEN'
bot_Username = '@YOUR Usernam BOT'




async def start_comend(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello ! Thanks For Chat Ghost . I am Ghost . ')

async def help_comend(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am Ghost ! How can I Help You ? Please Type send . ')
    
async def custom_comend(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This Is Custom Comend!. ')


def hndel_repons(texe:str)-> str:
    prosess: str = texe.lower()

    if 'hello' in prosess:
        return 'Hey Hello Baabeee hahaha .'
    
    if 'how are you' in prosess:
        return 'Thanks I Am Okeyy'
    
    if 'salam' in prosess:
        return 'salam khobi ?  '

    if 'khobi' in prosess:
        return 'mersi  '
    
    if 'mersi' in prosess:
        return 'Mokhlesam .'
    
    if 'Admin' in prosess:
        return ' Joooonn ?'
    
    
async def hndel_messeg(update:Update , context:ContextTypes.DEFAULT_TYPE):
    mssg_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User {update.message.chat_id} in {mssg_type}: "{text}"')

    if mssg_type == 'group':
        if bot_Username in text:
            neew_text: str = text.replace(bot_Username, '').strip()
            repsoe: str = hndel_repons(neew_text)
        else:
            return
    else:
        repsoe: str = hndel_repons(text)
    
    print('Bot:' , repsoe)
    await update.message.reply_text(repsoe)

async def Error(update:Update , context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} Errorr {context.error}')

if __name__ == '__main__':
    print('Starting Bot... ')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start' , start_comend))
    app.add_handler(CommandHandler('help' , help_comend))
    app.add_handler(CommandHandler('custom' , custom_comend))


    # Messages
    app.add_handler(MessageHandler(filters.TEXT, hndel_messeg))

    # Errors
    app.add_error_handler(Error)

    # Polls The Bot
    print('Polling...')
    app.run_polling(poll_interval=3)




