from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🔥 Институты
INSTITUTES = [
    "ГИ", "ИБМИ", "ИБО", "ИЭУ", "ИФКИ", "ИКН", "ИНМ", "ИТ", "ПИШМАСТ"
]

# 🔥 Количество курсов в каждом институте
COURSES = {
    "ГИ": [5, 2],    # 5 курсов + 2 магистратуры
    "ИНМ": [4, 1],   # 4 курса + 1 магистратура
    "default": [4, 2] # Остальные: 4 курса + 2 магистратуры
}


# 📌 Функция создания клавиатуры институтов
def get_institutes_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура для выбора института."""
    keyboard = InlineKeyboardMarkup(row_width=3)

    buttons = [InlineKeyboardButton(inst, callback_data=f"inst_{inst}") for inst in INSTITUTES]

    for i in range(0, len(buttons), 3):
        keyboard.inline_keyboard.append(buttons[i:i + 3])

    # Добавляем кнопку "Назад"
    keyboard.inline_keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back_main")])

    return keyboard


# 📌 Функция создания клавиатуры курсов
def get_courses_keyboard(institute: str) -> InlineKeyboardMarkup:
    """Клавиатура для выбора курса."""
    course_count, master_count = COURSES.get(institute, COURSES["default"])
    
    keyboard = InlineKeyboardMarkup(row_width=2)

    # Бакалавриат
    for i in range(1, course_count + 1):
        keyboard.insert(InlineKeyboardButton(f"{i} курс", callback_data=f"course_{institute}_{i}"))

    # Магистратура
    for i in range(1, master_count + 1):
        keyboard.insert(InlineKeyboardButton(f"{i} маг", callback_data=f"course_{institute}_m{i}"))

    # Кнопка "Назад"
    keyboard.inline_keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data="back_institutes")])

    return keyboard


# 📌 Функция клавиатуры подгрупп
def get_subgroups_keyboard(group: str, institute: str, subgroups: list) -> InlineKeyboardMarkup:
    """Клавиатура выбора подгруппы."""
    keyboard = InlineKeyboardMarkup()

    for sub in subgroups:
        keyboard.insert(InlineKeyboardButton(f"Подгруппа {sub}", callback_data=f"subgroup_{group}_{institute}_{sub}"))

    keyboard.insert(InlineKeyboardButton("🟢 Все подгруппы", callback_data=f"subgroup_{group}_{institute}_all"))
    keyboard.inline_keyboard.append([InlineKeyboardButton("🔙 Назад", callback_data=f"back_courses_{institute}")])

    return keyboard


# 📌 Функция клавиатуры подтверждения сохранения
def get_save_confirmation_keyboard(group: str, subgroup: str, institute: str) -> InlineKeyboardMarkup:
    """Клавиатура подтверждения сохранения."""
    keyboard = InlineKeyboardMarkup()

    keyboard.inline_keyboard.append([
        InlineKeyboardButton("✅ Да", callback_data=f"save_{group}_{subgroup}_{institute}"),
        InlineKeyboardButton("❌ Нет", callback_data="cancel_save")
    ])

    return keyboard
