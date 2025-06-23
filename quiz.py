from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio
from data.questions import (
    quiz_questions_a1_1,
    quiz_questions_a1_2,
    quiz_questions_a1_3,
    quiz_questions_a1_4,
    quiz_questions_a1_5,
    quiz_questions_a1_6,
    quiz_questions_a1_7,
    quiz_questions_a1_8,
    quiz_questions_a1_9,
    quiz_questions_a1_10,
    quiz_questions_a1_11,
    quiz_questions_a1_12
)


videos_a1_1 = [
    "https://youtu.be/ry9wE7IM4D4?si=9t36YBRh39efI9ct",
    "https://youtu.be/A_rEqGmFCdo?si=3Mm_92uoJVWvykgY",
    "https://youtu.be/kleB-0jmpUo?si=FCzFTc_yG6zt5EWY"
]

user_progress = {}
user_quiz_progress = {}

async def handle_a1_1_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_1":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_1):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_a1_1")]
            ])
        )

    elif data == "start_test_a1_1":
        await start_quiz_a1_1(update, context)


async def start_quiz_a1_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_a1_1(user_id, query, context)


async def send_quiz_question_a1_1(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_1):
        score = progress["score"]
        total = len(quiz_questions_a1_1)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.1", callback_data="start_a1_1")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.1", callback_data="start_a1_1")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.2", callback_data="start_a1_2")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_1[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_1_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_a1_1_0_2
    parts = data.split("_")
    # parts = ["quiz", "a1", "1", "0", "2"]
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_1[q_idx]
    if selected_option == question["correct_option"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_a1_1(user_id, query, context)

videos_a1_2 = [
    "https://youtu.be/QbFOcLjFKuI?si=Uo8iA0DlAq--RgDV",
    "https://youtu.be/fPPoDWleo3U?si=h10IX1nFookGRCcN",
    "https://youtu.be/AKzAjQrdh1w?si=9hF_8f3ibXkOtZT3"
]


async def handle_a1_2_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_2":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_2):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test2")]
            ])
        )

    elif data == "start_test2":
        await start_quiz2(update, context)

async def start_quiz2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_2(user_id, query, context)


async def send_quiz_questions_a1_2(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_2):
        score = progress["score"]
        total = len(quiz_questions_a1_2)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.2", callback_data="start_a1_2")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.2", callback_data="start_a1_2")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.3", callback_data="start_a1_3")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_2[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_2_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_2_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_2[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_2(user_id, query, context)



videos_a1_3 = [
    "https://youtu.be/yLpnnrn_kBg?si=lJh7LVDbZs4N4ICw",
    "https://youtu.be/9sVNHJQ0h08?si=zRLy-nkpDjNMs2id",
    "https://youtu.be/8XLQawtJIA4?si=eHd2X5zSUuTHEJEa"
]
async def handle_a1_3_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_3":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_3):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test3")]
            ])
        )

    elif data == "start_test3":
        await start_quiz3(update, context)

async def start_quiz3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_3(user_id, query, context)


async def send_quiz_questions_a1_3(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_3):
        score = progress["score"]
        total = len(quiz_questions_a1_3)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.3", callback_data="start_a1_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.3", callback_data="start_a1_3")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.4", callback_data="start_a1_4")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_3[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_3_{q_idx}_{i}")]
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

async def handle_quiz_answer_a1_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_3_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_3[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_3(user_id, query, context)

videos_a1_4 = [
    "https://www.youtube.com/watch?v=B3xJIlhIQ3Q&list=PLlf4N_2YLp7is06ePwns2AXu0oIRK3lCo&index=11",
    "https://www.youtube.com/watch?v=Qv-lluGDyxg&list=PLlf4N_2YLp7is06ePwns2AXu0oIRK3lCo&index=12",
    "https://www.youtube.com/watch?v=PSXNe540nfg&list=PLlf4N_2YLp7is06ePwns2AXu0oIRK3lCo&index=13"
]

async def handle_a1_4_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_4":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_4):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test4")]
            ])
        )

    elif data == "start_test4":
        await start_quiz4(update, context)

async def start_quiz4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_4(user_id, query, context)

async def send_quiz_questions_a1_4(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_4):
        score = progress["score"]
        total = len(quiz_questions_a1_4)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.4", callback_data="start_a1_4")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.4", callback_data="start_a1_4")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.5", callback_data="start_a1_5")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_4[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_4_{q_idx}_{i}")]
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

async def handle_quiz_answer_a1_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_4_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_4[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_4(user_id, query, context)

videos_a1_5 = [
    "https://www.youtube.com/live/kurgC_KVECk?si=oflu7nRoxk-Kgdjv",
    "https://www.youtube.com/live/Tk60ucAMnyE?si=29jweUJdVu6jN8kc",
    "https://www.youtube.com/live/pGxDwURqISM?si=aWiGtERSyBCp_du_"
]
async def handle_a1_5_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_5":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_5):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test5")]
            ])
        )

    elif data == "start_test5":
        await start_quiz5(update, context)

async def start_quiz5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_5(user_id, query, context)
async def send_quiz_questions_a1_5(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_5):
        score = progress["score"]
        total = len(quiz_questions_a1_5)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.5", callback_data="start_a1_5")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.5", callback_data="start_a1_5")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.6", callback_data="start_a1_6")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_5[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_5_{q_idx}_{i}")]
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
async def handle_quiz_answer_a1_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_5_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_5[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_5(user_id, query, context)
videos_a1_6 = [
    "https://www.youtube.com/live/CKRaUuMhL8s?si=I5Q1X2H5McqrQuvb",
    "https://www.youtube.com/live/URT_CAGA8DA?si=Boxi7VislbkshXKo",
    "https://www.youtube.com/live/SYOwg2JX6T8?si=RRR6MPWtfDpc66HA"
]

async def handle_a1_6_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_6":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_6):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test6")]
            ])
        )

    elif data == "start_test6":
        await start_quiz6(update, context)


async def start_quiz6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_6(user_id, query, context)


async def send_quiz_questions_a1_6(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_6):
        score = progress["score"]
        total = len(quiz_questions_a1_6)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.6", callback_data="start_a1_6")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.6", callback_data="start_a1_6")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.7", callback_data="start_a1_7")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_6[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_6_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_6_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_6[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_6(user_id, query, context)
videos_a1_7 = [
    "https://www.youtube.com/live/X7eNaJLwXe8?si=j2tz9EMJmxpvMYxx",
    "https://www.youtube.com/live/EvFqPjIJFJk?si=2d_gItHeVbaL802z",
    "https://www.youtube.com/live/f6osQlbj0RA?si=lfwPM9cN6z09Xfuy"
]

async def handle_a1_7_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_7":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_7):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test7")]
            ])
        )

    elif data == "start_test7":
        await start_quiz7(update, context)


async def start_quiz7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_7(user_id, query, context)


async def send_quiz_questions_a1_7(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_7):
        score = progress["score"]
        total = len(quiz_questions_a1_7)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.7", callback_data="start_a1_7")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.7", callback_data="start_a1_7")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.8", callback_data="start_a1_8")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_7[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_7_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_7_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_7[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_7(user_id, query, context)
videos_a1_8 = [
    "https://youtu.be/5RkVSX6jmfI?si=1yPBmgok_GNFt18D",
    "https://youtu.be/jJY23_IXpk8?si=Q9p-6m3_lSKQI5jx",
    "https://youtu.be/bxSNLTuuJ4Y?si=q1lPp2MfS1jFN_ri"
]

async def handle_a1_8_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_8":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_8):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test8")]
            ])
        )

    elif data == "start_test8":
        await start_quiz8(update, context)


async def start_quiz8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_8(user_id, query, context)


async def send_quiz_questions_a1_8(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_8):
        score = progress["score"]
        total = len(quiz_questions_a1_8)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.8", callback_data="start_a1_8")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.8", callback_data="start_a1_8")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.9", callback_data="start_a1_9")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_8[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_8_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_8_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_8[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_8(user_id, query, context)
videos_a1_9 = [
    "https://youtu.be/-aEImgmlhYg?si=x5unCD-pUMsLagM6",
    "https://youtu.be/uvkKj1C3jPs?si=nauXsnzr75Bc2huj",
    "https://youtu.be/o--F0lWsxOs?si=9afnFh61kpGHlTOf"
]

async def handle_a1_9_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_9":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_9):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test9")]
            ])
        )

    elif data == "start_test9":
        await start_quiz9(update, context)


async def start_quiz9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_9(user_id, query, context)


async def send_quiz_questions_a1_9(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_9):
        score = progress["score"]
        total = len(quiz_questions_a1_9)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.9", callback_data="start_a1_9")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.9", callback_data="start_a1_9")],
                [InlineKeyboardButton("➡ Բարձրանալ A1.10", callback_data="start_a1_10")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_9[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_9_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_9_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_9[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_9(user_id, query, context)
videos_a1_10 = [
    "https://youtu.be/XcIi_Ubwhic?si=ZNHbcq_EaOPfEB5T",
    "https://youtu.be/qHYMZDDSvjg?si=bJ-No942B2r3l9QQ",
    "https://youtu.be/5uIaZqmmoPI?si=ppqnE7EGqFBZIdAF"
]

async def handle_a1_10_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_10":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_10):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test10")]
            ])
        )

    elif data == "start_test10":
        await start_quiz10(update, context)


async def start_quiz10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_10(user_id, query, context)


async def send_quiz_questions_a1_10(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_10):
        score = progress["score"]
        total = len(quiz_questions_a1_10)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.10", callback_data="start_a1_10")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.10", callback_data="start_a1_10")],
                [InlineKeyboardButton("➡ Բարձրանալ  A1.11", callback_data="start_a1_11")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_10[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_10_{q_idx}_{i}")]
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
async def handle_quiz_answer_a1_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_10_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_10[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_10(user_id, query, context)

videos_a1_11 = [
    "https://youtu.be/pra0rhG5YwU?si=K8GupHSD850KfCJf",
    "https://youtu.be/ae2Wx1n9aWU?si=2OFmImSQ2yey0vhs",
    "https://youtu.be/Vmh8orz3Hkc?si=rOxDTAwxrYK_OFpV"
]

async def handle_a1_11_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_11":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_11):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test11")]
            ])
        )

    elif data == "start_test11":
        await start_quiz11(update, context)


async def start_quiz11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_11(user_id, query, context)


async def send_quiz_questions_a1_11(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_11):
        score = progress["score"]
        total = len(quiz_questions_a1_11)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.11", callback_data="start_a1_11")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.11", callback_data="start_a1_11")],
                [InlineKeyboardButton("➡  Բարձրանալ A1.12", callback_data="start_a1_12")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_11[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_11_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_11_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_11[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_11(user_id, query, context)
videos_a1_12 = [
    "https://youtu.be/Qzl3KB_nC0Q?si=Oa1UskUSNmnCqwWN",
    "https://youtu.be/-kQOkZJFRYs?si=wYxT-r6S1j_aaZKO",
    "https://youtu.be/ed_FyIs-vQA?si=IwXXQGT4xwM4nczz"
]

async def handle_a1_12_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_a1_12":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_a1_12):
            await context.bot.send_message(
                chat_id=user_id,
                text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}"
            )
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք  բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test12")]
            ])
        )

    elif data == "start_test12":
        await start_quiz12(update, context)


async def start_quiz12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_questions_a1_12(user_id, query, context)


async def send_quiz_questions_a1_12(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_a1_12):
        score = progress["score"]
        total = len(quiz_questions_a1_12)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.12", callback_data="start_a1_12")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել A1.12", callback_data="start_a1_12")],
                [InlineKeyboardButton("➡ Անցնել A2 մակարդակ 🎉", callback_data="start_a2_1")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_a1_12[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_a1_12_{q_idx}_{i}")]
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


async def handle_quiz_answer_a1_12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # пример: quiz_a1_12_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    try:
        q_idx = int(parts[3])
        selected_option = int(parts[4])
    except ValueError:
        return

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_a1_12[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_questions_a1_12(user_id, query, context)
