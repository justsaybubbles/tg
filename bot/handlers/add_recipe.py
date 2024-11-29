from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from config import RECIPES_FILE

class AddRecipeHandler(ConversationHandler):
    def __init__(self):
        super().__init__(
            entry_points=[CommandHandler('add_recipe', self.start)],
            states={
                1: [MessageHandler(Filters.text & ~Filters.command, self.handle_message)]
            },
            fallbacks=[]
        )
        
    def start(self, update, context):
        update.message.reply_text('Отправь мне ссылку на рецепт или текст рецепта.')
        return 1
    
    def handle_message(self, update, context):
        message = update.message.text
        if message.startswith('http'):
            # Обработать ссылку
            pass
        else:
            # Обработать текст
            pass
        update.message.reply_text('Рецепт получен. Что дальше?')
        return ConversationHandler.END