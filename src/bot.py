import os
from telegram import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from db import init_db, add_class, get_schedule, clear_schedule
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()
TOKEN = "7068683215:AAHHTm7NX_z2T0OW-4k_73D4MbCb9v3ZsKM"

init_db()

WEEKDAYS = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
user_states = {}

init_db()


async def start(update, context):
    keyboard = [
        [KeyboardButton("➕ Добавить пару")],
        [KeyboardButton("📅 Расписание")],
        [KeyboardButton("🗑️ Очистить всё")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет! Я бот для расписания пар 😊", reply_markup=reply_markup)


async def handle_text(update, context):
    chat_id = str(update.message.chat.id)
    text = update.message.text.strip()

    print(f"Received text: {text}")  

    if text == "➕ Добавить пару":
        user_states[chat_id] = {"step": "choose_day"}
        keyboard = [[KeyboardButton(day.title())] for day in WEEKDAYS]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выбери день недели:", reply_markup=reply_markup)
        return

    if text in WEEKDAYS:
        print(f"Day selected: {text}")  # Логируем выбранный день
        if chat_id not in user_states or user_states[chat_id].get("step") != "choose_day":
            await update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте снова.")
            return
        user_states[chat_id] = {"step": "enter_name", "day": text}
        print(f"User state after choosing day: {user_states[chat_id]}")  # Логируем состояние после выбора дня
        await update.message.reply_text(f"Вы выбрали {text}. Теперь введите название пары:", reply_markup=ReplyKeyboardRemove())
        return


    if user_states.get(chat_id, {}).get("step") == "enter_name":
        print(f"User state before entering name: {user_states[chat_id]}")  # Логируем состояние до ввода названия пары
        user_states[chat_id]["name"] = text
        user_states[chat_id]["step"] = "enter_time"
        await update.message.reply_text("Введите время пары в формате HH:MM:")
        return

    # Обработка ввода времени
    if user_states.get(chat_id, {}).get("step") == "enter_time":
        try:
            time = text.strip()
            user_states[chat_id]["time"] = time
            user_states[chat_id]["step"] = "enter_notify"
            await update.message.reply_text("За сколько минут до начала пары напоминать? (например, 10, 30, 60)")
        except ValueError:
            await update.message.reply_text("Неверный формат времени. Введите время в формате HH:MM.")
        return


    if user_states.get(chat_id, {}).get("step") == "enter_notify":
        try:
            notify = int(text)
            user_states[chat_id]["notify"] = notify

            add_class(chat_id, user_states[chat_id]["day"], user_states[chat_id]["name"], user_states[chat_id]["time"], notify)
            await update.message.reply_text("✅ Пара добавлена!")
            del user_states[chat_id]  
            
            keyboard = [
                [KeyboardButton("➕ Добавить пару")],
                [KeyboardButton("📅 Расписание")],
                [KeyboardButton("🗑️ Очистить всё")]
            ]
            reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
            await update.message.reply_text("Вы можете добавить еще пару или посмотреть расписание.", reply_markup=reply_markup)
        except ValueError:
            await update.message.reply_text("Введите только число (например, 10).")
        return

    if text == "📅 Расписание":
        schedule = get_schedule(chat_id)
        if schedule:
            schedule_text = "\n".join([f"{item['day']} - {item['name']} в {item['time']} (напоминание за {item['notify']} минут)"
                                      for item in schedule])
            await update.message.reply_text(f"Ваше расписание:\n\n{schedule_text}")
        else:
            await update.message.reply_text("Ваше расписание пусто.")
        return


    if text == "🗑️ Очистить всё":
        clear_schedule(chat_id)
        await update.message.reply_text("Ваше расписание очищено.")
        return


    await update.message.reply_text("Произошла ошибка. Пожалуйста, попробуйте снова.")


async def error_handler(update, context):
    print(f"Error: {context.error}")  


application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
application.add_error_handler(error_handler)  
application.run_polling()