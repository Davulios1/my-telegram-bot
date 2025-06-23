from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio
from data.questions import (
    quiz_questions_b2_1,
    quiz_questions_b2_2,
    quiz_questions_b2_3,
    quiz_questions_b2_4,
    quiz_questions_b2_5,
    quiz_questions_b2_6,
    quiz_questions_b2_7,
    quiz_questions_b2_8,
    quiz_questions_b2_9,
    quiz_questions_b2_10,

)


videos_b2_1 = [
    "https://youtu.be/vrdH7Yrjfdc?si=KL4Iilmj1x_WwSyO",
    "https://youtu.be/Qzl3KB_nC0Q?si=05LF61ZI9LN3lU3c",
    "https://youtu.be/NfRLxgcZGso?si=pczBcamVKN4LMRD8"
]
# Прогресс пользователей
user_progress = {}
user_quiz_progress = {}

# Обработка кнопки "Սկսել B2.1 մակարդակը"
async def handle_b2_1_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_1":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_1):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_1")]
            ])
        )

    elif data == "start_test_b2_1":
        await start_quiz_b2_1(update, context)


# Запуск теста
async def start_quiz_b2_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_1(user_id, query, context)


# Отправка вопроса
async def send_quiz_question_b2_1(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_1):
        score = progress["score"]
        total = len(quiz_questions_b2_1)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.1", callback_data="start_b2_1")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.1", callback_data="start_b2_1")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.2", callback_data="start_b2_2")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_1[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_1_{q_idx}_{i}")]
        for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# Обработка ответов
async def handle_quiz_answer_b2_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_1_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_1[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_1(user_id, query, context)
videos_b2_2 = [
    "https://www.youtube.com/live/f6osQlbj0RA?si=IkgfVnIz_n-aU8kX",
    "https://www.youtube.com/live/VFFNoIbS6r4?si=2W2ZrUGVEt41WNY9",
    "https://www.youtube.com/live/3bamePxfxWM?si=zJESgYuKgmWI6wg3"
]

# Обработка кнопки "Սկսել B2.2 մակարդակը"
async def handle_b2_2_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_2":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_2):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_2")]
            ])
        )

    elif data == "start_test_b2_2":
        await start_quiz_b2_2(update, context)


# Запуск теста
async def start_quiz_b2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_2(user_id, query, context)


# Отправка вопроса
async def send_quiz_question_b2_2(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_2):
        score = progress["score"]
        total = len(quiz_questions_b2_2)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.2", callback_data="start_b2_2")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.2", callback_data="start_b2_2")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.3", callback_data="start_b2_3")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_2[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_2_{q_idx}_{i}")]
        for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# Обработка ответов
async def handle_quiz_answer_b2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_2_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_2[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_2(user_id, query, context)
videos_b2_3 = [
    "https://youtu.be/gMU4Iv1gmr4?si=Ps-LzWNtfhuejumZ",
    "https://youtu.be/bP1_gf8mlNQ?si=d6Vwc8SVoT2g3Xk0",
    "https://youtu.be/XcIi_Ubwhic?si=1ZfvLu51dCnvxQ9a"
]

async def handle_b2_3_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_3":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_3):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_3")]
            ])
        )

    elif data == "start_test_b2_3":
        await start_quiz_b2_3(update, context)


async def start_quiz_b2_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_3(user_id, query, context)


async def send_quiz_question_b2_3(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_3):
        score = progress["score"]
        total = len(quiz_questions_b2_3)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.3", callback_data="start_b2_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.3", callback_data="start_b2_3")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.4", callback_data="start_b2_4")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_3[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_3_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_3_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_3[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_3(user_id, query, context)
videos_b2_4 = [
    "https://youtu.be/E8xg1V03cEY?si=wkSmPNIs_-_59leF",
    "https://youtu.be/Ucu3a5R6ZXg?si=ATtJOwja06feag5J",
    "https://youtu.be/CmTTX5Su0Dw?si=-BJxrjeKNmGiiLPA"
]

async def handle_b2_4_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_4":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_4):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_4")]
            ])
        )

    elif data == "start_test_b2_4":
        await start_quiz_b2_4(update, context)


async def start_quiz_b2_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_4(user_id, query, context)


async def send_quiz_question_b2_4(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_4):
        score = progress["score"]
        total = len(quiz_questions_b2_4)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.4", callback_data="start_b2_4")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.4", callback_data="start_b2_4")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.5", callback_data="start_b2_5")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_4[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_4_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_4_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_4[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_4(user_id, query, context)
videos_b2_5 = [
    "https://youtu.be/ae2Wx1n9aWU?si=qf1lV3xkxT8fzK7R",
    "https://www.youtube.com/live/XEwN3BjR7lk?si=NxFn6dNQpaW2vMRe",
    "https://youtu.be/7v9bO94_MXg?si=lqgAHrC6WN0urisF"
]

async def handle_b2_5_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_5":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_5):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_5")]
            ])
        )

    elif data == "start_test_b2_5":
        await start_quiz_b2_5(update, context)


async def start_quiz_b2_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_5(user_id, query, context)


async def send_quiz_question_b2_5(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_5):
        score = progress["score"]
        total = len(quiz_questions_b2_5)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.5", callback_data="start_b2_5")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.5", callback_data="start_b2_5")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.6", callback_data="start_b2_6")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_5[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_5_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_5_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_5[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_5(user_id, query, context)
videos_b2_6 = [
    "https://youtu.be/qnN70PGEDAA?si=tCzRKyN0fSlf4K_U",
    "https://youtu.be/oVfseLgVm9o?si=psTYnk985KmcvQOA",
    "https://youtu.be/zbRWB8aP4Ww?si=tuedC_DamVrBhuGB"
]

async def handle_b2_6_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_6":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_6):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_6")]
            ])
        )

    elif data == "start_test_b2_6":
        await start_quiz_b2_6(update, context)


async def start_quiz_b2_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_6(user_id, query, context)


async def send_quiz_question_b2_6(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_6):
        score = progress["score"]
        total = len(quiz_questions_b2_6)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.6", callback_data="start_b2_6")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.6", callback_data="start_b2_6")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.7", callback_data="start_b2_7")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_6[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_6_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_6_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_6[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_6(user_id, query, context)
videos_b2_7 = [
    "https://youtu.be/GesblJ1gnZ8?si=bu4_BrJ8qqYrEFgw",
    "https://youtu.be/qHYMZDDSvjg?si=cEia-3Fu3fo-f4CU",
    "https://youtu.be/EjWhQ9fw0Co?si=QOdBPnK0M-M2xYYR"
]

async def handle_b2_7_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_7":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_7):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_7")]
            ])
        )

    elif data == "start_test_b2_7":
        await start_quiz_b2_7(update, context)


async def start_quiz_b2_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_7(user_id, query, context)


async def send_quiz_question_b2_7(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_7):
        score = progress["score"]
        total = len(quiz_questions_b2_7)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.7", callback_data="start_b2_7")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.7", callback_data="start_b2_7")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.8", callback_data="start_b2_8")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_7[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_7_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_7_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_7[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_7(user_id, query, context)
videos_b2_8 = [
    "https://youtu.be/6_kEM2vaR68?si=kIO9kPXC25yNmClz",
    "https://youtu.be/L1i38Z0eNLA?si=ig7B9TWPVLeHAeX2",
    "https://youtu.be/6_kEM2vaR68?si=QGOcpVVc5Bu7yNVh"
]

async def handle_b2_8_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_8":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_8):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_8")]
            ])
        )

    elif data == "start_test_b2_8":
        await start_quiz_b2_8(update, context)


async def start_quiz_b2_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_8(user_id, query, context)


async def send_quiz_question_b2_8(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_8):
        score = progress["score"]
        total = len(quiz_questions_b2_8)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.8", callback_data="start_b2_8")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.8", callback_data="start_b2_8")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.9", callback_data="start_b2_9")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_8[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_8_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_8_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_8[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_8(user_id, query, context)
videos_b2_9 = [
    "https://youtu.be/-kQOkZJFRYs?si=eTh5kC0Nq3b1-6_X",
    "https://youtu.be/PPXpR2PDMhM?si=Vq3SBAyuwu7q-3SI",
    "https://youtu.be/B4CeWomYWeM?si=93vY3xRawBR-mIcS"
]

async def handle_b2_9_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_9":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_9):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_9")]
            ])
        )

    elif data == "start_test_b2_9":
        await start_quiz_b2_9(update, context)


async def start_quiz_b2_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_9(user_id, query, context)


async def send_quiz_question_b2_9(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_9):
        score = progress["score"]
        total = len(quiz_questions_b2_9)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.9", callback_data="start_b2_9")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.9", callback_data="start_b2_9")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.10", callback_data="start_b2_10")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_9[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_9_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_9_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_9[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_9(user_id, query, context)
videos_b2_10 = [
    "https://youtu.be/5kYMy8nKB8A?si=M1yL8RuJUCmEGjl2",
    "https://youtu.be/7v9bO94_MXg?si=HrxSyGfypHpbQ0sn",
    "https://youtu.be/LJ_4zlrDYmA?si=uFF6YDxsJ4gGXhlT"
]

async def handle_b2_10_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b2_10":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_b2_10):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b2_10")]
            ])
        )

    elif data == "start_test_b2_10":
        await start_quiz_b2_10(update, context)


async def start_quiz_b2_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b2_10(user_id, query, context)


async def send_quiz_question_b2_10(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b2_10):
        score = progress["score"]
        total = len(quiz_questions_b2_10)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.10", callback_data="start_b2_10")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B2.10", callback_data="start_b2_10")],
                [InlineKeyboardButton("➡ Բարձրանալ C1.1", callback_data="start_c1_1")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b2_10[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b2_10_{q_idx}_{i}")] for i, opt in enumerate(options)
    ]

    if query:
        await query.edit_message_text(
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await context.bot.send_message(
            chat_id=user_id,
            text=f"❓ Հարց {q_idx + 1}: {question['question']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


async def handle_quiz_answer_b2_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_b2_10_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b2_10[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b2_10(user_id, query, context)
