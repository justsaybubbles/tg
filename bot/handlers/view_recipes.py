from telegram.ext import ConversationHandler, CommandHandler, MessageHandler, Filters
from config import RECIPES_FILE

class ViewRecipesHandler(ConversationHandler):
    def __init__(self):
        super().__init__(
            entry_points=[CommandHandler('view_recipes', self.start)],
            states={},
            fallbacks=[]
        )
        
    def start(self, update, context):
        update.message.reply_text('Выбери категорию:')
        keyboard = [['Основные блюда'], ['Вторые блюда'], ['Выпечка'], ['Напитки'], ['Лайфхаки']]
        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
        update.message.reply_text('Категории:', reply_markup=reply_markup)
        return 1
    
    def handle_category(self, update, context):
        category = update.message.text
        # Показать рецепты из выбранной категории
        pass