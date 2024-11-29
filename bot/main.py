from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers.add_recipe import AddRecipeHandler
from handlers.view_recipes import ViewRecipesHandler
from config import TOKEN

def main():
    updater = Updater(TOKEN, use_context=True)
    
    dp = updater.dispatcher
    
    # Обработчики команд
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(AddRecipeHandler())
    dp.add_handler(ViewRecipesHandler())
    
    # Запуск бота
    updater.start_polling()
    updater.idle()

def start(update, context):
    update.message.reply_text(
        'Привет! Этот бот помогает управлять твоими рецептами.'
    )

if __name__ == '__main__':
    main()