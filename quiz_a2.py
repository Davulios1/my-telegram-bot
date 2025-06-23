from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio
from data.questions import (
    quiz_questions_a2_1,
    quiz_questions_a2_2,
    quiz_questions_a2_3,
    quiz_questions_a2_4,
    quiz_questions_a2_5,
    quiz_questions_a2_6,
    quiz_questions_a2_7,
    quiz_questions_a2_8,
    quiz_questions_a2_9,
    quiz_questions_a2_10,
    quiz_questions_a2_11,
    quiz_questions_a2_12
)


videos_a2_1 = [
    "https://www.youtube.com/live/kurgC_KVECk?si=tFpAD4ZPyoHu-e4I",
    "https://youtu.be/pra0rhG5YwU?si=89JawjKk9qPLIWfG",
    "https://youtu.be/zbRWB8aP4Ww?si=GVFPdvk6_TObrX5R"
]

# Прогресс пользователей
user_progress = {}
user_quiz_progress = {}


# Обработка кнопки "Սկսել A2.1 մակարդակը"
async def handle_a2_1_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_1":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_1):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_1")]
            ])
        )

    elif data == "start_test_a2_1":
        await start_quiz_a2_1(update, context)


# Запуск теста
async def start_quiz_a2_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_1(user_id, query, context)


# Отправка вопроса
async def send_quiz_question_a2_1(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_1):
        score = progress["score"]
        total = len(quiz_questions_a2_1)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.1", callback_data="start_a2_1")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.1", callback_data="start_a2_1")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.2", callback_data="start_a2_2")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_1[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_1_{q_idx}_{i}")]
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
async def handle_quiz_answer_a2_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_1_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_1[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_1(user_id, query, context)
videos_a2_2 = [
    "https://www.youtube.com/live/EvFqPjIJFJk?si=7UBCYamR2rguz59j",
    "https://youtu.be/xxO9THWENnM?si=hhgIPifvp5EQFgZs",
    "https://youtu.be/9lfr_eqJ-h0?si=JWlamyd82LjJYyhi"
]

# Обработка кнопки "Սկսել A2.2 մակարդակը"
async def handle_a2_2_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_2":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_2):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_2")]
            ])
        )

    elif data == "start_test_a2_2":
        await start_quiz_a2_2(update, context)


# Запуск теста
async def start_quiz_a2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_2(user_id, query, context)


# Отправка вопроса
async def send_quiz_question_a2_2(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_2):
        score = progress["score"]
        total = len(quiz_questions_a2_2)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.2", callback_data="start_a2_2")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.2", callback_data="start_a2_2")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.3", callback_data="start_a2_3")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_2[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_2_{q_idx}_{i}")]
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
async def handle_quiz_answer_a2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_2_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_2[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_2(user_id, query, context)

videos_a2_3 = [
    "https://youtu.be/hYuydKA9INw?si=WeKG43fVV1qHFAFx",
    "https://youtu.be/whTS9HhqTHo?si=8JPa6bg3kdIkL7Yn",
    "https://youtu.be/GOz8xoDhf74?si=oA8Ryd7FaJ4JIRpN"
]

# Обработка кнопки "Սկսել A2.3 մակարդակը"
async def handle_a2_3_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_3":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_3):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_3")]
            ])
        )

    elif data == "start_test_a2_3":
        await start_quiz_a2_3(update, context)


# Запуск теста
async def start_quiz_a2_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_3(user_id, query, context)


# Отправка вопроса
async def send_quiz_question_a2_3(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_3):
        score = progress["score"]
        total = len(quiz_questions_a2_3)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.3", callback_data="start_a2_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.3", callback_data="start_a2_3")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.4", callback_data="start_a2_4")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_3[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_3_{q_idx}_{i}")]
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
async def handle_quiz_answer_a2_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_3_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_3[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_3(user_id, query, context)
videos_a2_4 = [
    "https://youtu.be/jf-LDwAzFHU?si=EXI67d9TDUjiSEvN",
    "https://youtu.be/c3Wqb0WcaAQ?si=tTPJtEAaNerMhLMg",
    "https://youtu.be/mFe99sgQSZw?si=9-ybIvHDtxqIh0af"
]

async def handle_a2_4_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_4":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_4):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_4")]
            ])
        )

    elif data == "start_test_a2_4":
        await start_quiz_a2_4(update, context)

async def start_quiz_a2_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_4(user_id, query, context)

async def send_quiz_question_a2_4(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_4):
        score = progress["score"]
        total = len(quiz_questions_a2_4)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.4", callback_data="start_a2_4")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.4", callback_data="start_a2_4")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.5", callback_data="start_a2_5")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_4[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_4_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_4_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_4[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_4(user_id, query, context)
videos_a2_5 = [
    "https://youtu.be/mFe99sgQSZw?si=pQY-TWxRycw-73Xs",
    "https://youtu.be/ApiLQmH4lAY?si=gMfN_CCeHlHbC3WW",
    "https://youtu.be/XtYKNeHhk9U?si=BUMDKS89ZhRY92Qv"
]

async def handle_a2_5_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_5":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_5):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_5")]
            ])
        )

    elif data == "start_test_a2_5":
        await start_quiz_a2_5(update, context)

async def start_quiz_a2_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_5(user_id, query, context)

async def send_quiz_question_a2_5(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_5):
        score = progress["score"]
        total = len(quiz_questions_a2_5)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.5", callback_data="start_a2_5")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.5", callback_data="start_a2_5")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.6", callback_data="start_a2_6")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_5[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_5_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_5_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_5[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_5(user_id, query, context)
videos_a2_6 = [
    "https://youtu.be/XcIDX-Nd_Rc?si=atx2rBZng4rnke15",
    "https://youtu.be/6kRoGtuY7XE?si=u0equ0MsyRnrVL-I",
    "https://youtu.be/J6_q_TSOf6I?si=Q1Bfo3jPWqyU1sew"
]

async def handle_a2_6_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_6":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_6):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_6")]
            ])
        )

    elif data == "start_test_a2_6":
        await start_quiz_a2_6(update, context)

async def start_quiz_a2_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_6(user_id, query, context)

async def send_quiz_question_a2_6(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_6):
        score = progress["score"]
        total = len(quiz_questions_a2_6)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.6", callback_data="start_a2_6")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.6", callback_data="start_a2_6")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.7", callback_data="start_a2_7")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_6[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_6_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_6_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_6[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_6(user_id, query, context)
videos_a2_7 = [
    "https://youtu.be/j-5DN3GqzF4?si=kTqRNnrAmWjUcX43",
    "https://youtu.be/ed_FyIs-vQA?si=dz_O9Rypga8Aw0sX",
    "https://youtu.be/UtfuBZgeaNc?si=lLwfHd-ecCVa8oTS"
]

async def handle_a2_7_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_7":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_7):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_7")]
            ])
        )

    elif data == "start_test_a2_7":
        await start_quiz_a2_7(update, context)

async def start_quiz_a2_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_7(user_id, query, context)

async def send_quiz_question_a2_7(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_7):
        score = progress["score"]
        total = len(quiz_questions_a2_7)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.7", callback_data="start_a2_7")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.7", callback_data="start_a2_7")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.8", callback_data="start_a2_8")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_7[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_7_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_7_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_7[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_7(user_id, query, context)
videos_a2_8 = [
    "https://youtu.be/OAPx6bK1TAk?si=i-GMEIGpUEQta5-2",
    "https://youtu.be/vgnglp9oEDs?si=XrdUQhtgJtwJ95fC",
    "https://www.youtube.com/live/pGxDwURqISM?si=5df-nog9o1vT4tUb"
]

async def handle_a2_8_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_8":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_8):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_8")]
            ])
        )

    elif data == "start_test_a2_8":
        await start_quiz_a2_8(update, context)

async def start_quiz_a2_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_8(user_id, query, context)

async def send_quiz_question_a2_8(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_8):
        score = progress["score"]
        total = len(quiz_questions_a2_8)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.8", callback_data="start_a2_8")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.8", callback_data="start_a2_8")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.9", callback_data="start_a2_9")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_8[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_8_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_8_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_8[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_8(user_id, query, context)
videos_a2_9 = [
    "https://www.youtube.com/live/CKRaUuMhL8s?si=I9kYkNQ_BjdR9Z7q",
    "https://www.youtube.com/live/kurgC_KVECk?si=igUi58MUNlsZL_-r",
    "https://www.youtube.com/live/e6_JNsB7vuE?si=PSZ81MFYDpcuSi5Z"
]

async def handle_a2_9_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_9":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_9):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_9")]
            ])
        )

    elif data == "start_test_a2_9":
        await start_quiz_a2_9(update, context)

async def start_quiz_a2_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_9(user_id, query, context)

async def send_quiz_question_a2_9(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_9):
        score = progress["score"]
        total = len(quiz_questions_a2_9)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.9", callback_data="start_a2_9")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.9", callback_data="start_a2_9")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.10", callback_data="start_a2_10")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_9[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_9_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_9_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_9[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_9(user_id, query, context)
videos_a2_10 = [
    "https://www.youtube.com/live/URT_CAGA8DA?si=Erwt8GwpMcNvEpCV",
    "https://www.youtube.com/live/SYOwg2JX6T8?si=BU8lE5ORZJoRwEsA",
    "https://www.youtube.com/live/X7eNaJLwXe8?si=zzfzwGss-fjnXp7a"
]

async def handle_a2_10_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_10":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_10):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_10")]
            ])
        )

    elif data == "start_test_a2_10":
        await start_quiz_a2_10(update, context)

async def start_quiz_a2_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_10(user_id, query, context)

async def send_quiz_question_a2_10(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_10):
        score = progress["score"]
        total = len(quiz_questions_a2_10)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.10", callback_data="start_a2_10")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.10", callback_data="start_a2_10")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.11", callback_data="start_a2_11")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_10[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_10_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_10_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_10[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_10(user_id, query, context)
videos_a2_11 = [
    "https://youtu.be/4Hqc_pWzqxM?si=fvsTqyi-vi795Xit",
    "https://youtu.be/bxSNLTuuJ4Y?si=68SSXFh7LL2w-k-o",
    "https://www.youtube.com/live/Tk60ucAMnyE?si=N-SMLHreTgV73KW9"
]

async def handle_a2_11_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_11":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_11):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_11")]
            ])
        )

    elif data == "start_test_a2_11":
        await start_quiz_a2_11(update, context)

async def start_quiz_a2_11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_11(user_id, query, context)

async def send_quiz_question_a2_11(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_11):
        score = progress["score"]
        total = len(quiz_questions_a2_11)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.11", callback_data="start_a2_11")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.11", callback_data="start_a2_11")],
                [InlineKeyboardButton("➡ Բարձրանալ A2.12", callback_data="start_a2_12")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_11[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_11_{q_idx}_{i}")]
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

async def handle_quiz_answer_a2_11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_11_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_11[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_11(user_id, query, context)
videos_a2_12 = [
    "https://youtu.be/docVFBY1Jgc?si=AguC_xMQ9aPBRjjh",
    "https://youtu.be/j_0QU2yz0pg?si=A7gMfDfnuDtoiudJ",
    "https://youtu.be/-aEImgmlhYg?si=l4WdBlRs2ZGmOFBC"
]

# Обработка кнопки "Սկսել A2.12 մակարդակը"
async def handle_a2_12_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a2_12":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_a2_12):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a2_12")]
            ])
        )

    elif data == "start_test_a2_12":
        await start_quiz_a2_12(update, context)


# Սկսել թեստը
async def start_quiz_a2_12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a2_12(user_id, query, context)


# Ուղարկել հարցը
async def send_quiz_question_a2_12(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a2_12):
        score = progress["score"]
        total = len(quiz_questions_a2_12)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.12", callback_data="start_a2_12")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A2.12", callback_data="start_a2_12")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.1", callback_data="start_b1_1")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a2_12[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a2_12_{q_idx}_{i}")]
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


# Հասցեագրել պատասխանները
async def handle_quiz_answer_a2_12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_a2_12_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a2_12[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a2_12(user_id, query, context)

