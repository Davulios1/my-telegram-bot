from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio
from data.questions import (
    quiz_questions_c1_1,
    quiz_questions_c1_2,
    quiz_questions_c1_3,
    quiz_questions_c1_4,
    quiz_questions_c1_5,
)
videos_c1_1 = [
    "https://youtu.be/qnN70PGEDAA?si=f1__wlSfeoIBiV0M",
    "https://youtu.be/M2fTEShHBWs?si=HvdvgLClAM0BTptx",
    "https://youtu.be/5JgN9Adze6M?si=WJb2lEHHDWalKgNN"
]

user_progress = {}
user_quiz_progress = {}

async def handle_c1_1_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c1_1":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c1_1):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c1_1")]
            ])
        )

    elif data == "start_test_c1_1":
        await start_quiz_c1_1(update, context)


async def start_quiz_c1_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c1_1(user_id, query, context)


async def send_quiz_question_c1_1(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c1_1):
        score = progress["score"]
        total = len(quiz_questions_c1_1)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.1", callback_data="start_c1_1")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.1", callback_data="start_c1_1")],
                [InlineKeyboardButton("➡ Բարձրանալ C1.2", callback_data="start_c1_2")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c1_1[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c1_1_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c1_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c1_1_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c1_1[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c1_1(user_id, query, context)
videos_c1_2 = [
    "https://youtu.be/OzjYOfrfNZM?si=_Vavukf-156oPovD",
    "https://youtu.be/09eoAn2dZ_g?si=jb9xQ80qxoKhSMKy",
    "https://youtu.be/o3ZUMvh1Uow?si=FTIbsnMhxHe37GDr"
]

async def handle_c1_2_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c1_2":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c1_2):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c1_2")]
            ])
        )

    elif data == "start_test_c1_2":
        await start_quiz_c1_2(update, context)


async def start_quiz_c1_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c1_2(user_id, query, context)


async def send_quiz_question_c1_2(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c1_2):
        score = progress["score"]
        total = len(quiz_questions_c1_2)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.2", callback_data="start_c1_2")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.2", callback_data="start_c1_2")],
                [InlineKeyboardButton("➡ Բարձրանալ C1.3", callback_data="start_c1_3")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c1_2[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c1_2_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c1_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c1_2_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c1_2[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c1_2(user_id, query, context)
videos_c1_3 = [
    "https://youtu.be/ld0cp2aZ0rQ?si=yKNxJjqI0x1HIHPc",
    "https://youtu.be/ylKfQp4WESY?si=AocDez3zTcI_nMW9",
    "https://youtu.be/_k5ZL0VBUNY?si=jXc50LYHP4p1-hUe"
]

async def handle_c1_3_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c1_3":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c1_3):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c1_3")]
            ])
        )

    elif data == "start_test_c1_3":
        await start_quiz_c1_3(update, context)


async def start_quiz_c1_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c1_3(user_id, query, context)


async def send_quiz_question_c1_3(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c1_3):
        score = progress["score"]
        total = len(quiz_questions_c1_3)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.3", callback_data="start_c1_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.3", callback_data="start_c1_3")],
                [InlineKeyboardButton("➡ Բարձրանալ C1.4", callback_data="start_c1_4")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c1_3[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c1_3_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c1_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c1_3_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c1_3[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c1_3(user_id, query, context)
videos_c1_4 = [
    "https://youtu.be/licYodqcbeA?si=WOvNw1fwPieaJU-R",
    "https://youtu.be/_-9VMrLOEfo?si=G_s4db-VP6AwxNkx",
    "https://youtu.be/J6EO4CrTLBk?si=zc4mbDzOKDf9W0eZ"
]

async def handle_c1_4_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c1_4":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c1_4):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c1_4")]
            ])
        )

    elif data == "start_test_c1_4":
        await start_quiz_c1_4(update, context)


async def start_quiz_c1_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c1_4(user_id, query, context)


async def send_quiz_question_c1_4(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c1_4):
        score = progress["score"]
        total = len(quiz_questions_c1_4)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.4", callback_data="start_c1_4")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.4", callback_data="start_c1_4")],
                [InlineKeyboardButton("➡ Բարձրանալ C1.5", callback_data="start_c1_5")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c1_4[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c1_4_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c1_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c1_4_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c1_4[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c1_4(user_id, query, context)
videos_c1_5 = [
    "https://youtu.be/Y0XhuITT70o?si=47-p35U_R9poe9zD",
    "https://youtu.be/2vTByuQ9a78?si=Na4vhdQ4Tvo5uOr9",
    "https://youtu.be/tOUI9_deTjE?si=bTbxMXfUmLnrcjPh"
]

async def handle_c1_5_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c1_5":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c1_5):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c1_5")]
            ])
        )

    elif data == "start_test_c1_5":
        await start_quiz_c1_5(update, context)


async def start_quiz_c1_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c1_5(user_id, query, context)


async def send_quiz_question_c1_5(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c1_5):
        score = progress["score"]
        total = len(quiz_questions_c1_5)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.5", callback_data="start_c1_5")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C1.5", callback_data="start_c1_5")],
                [InlineKeyboardButton("➡ Բարձրանալ C2.1", callback_data="start_c2_1")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c1_5[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c1_5_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c1_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c1_5_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c1_5[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c1_5(user_id, query, context)
