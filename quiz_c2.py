from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio
from data.questions import (
    quiz_questions_c2_1,
    quiz_questions_c2_2,
    quiz_questions_c2_3,
    quiz_questions_c2_4,
    quiz_questions_c2_5,
)

videos_c2_1 = [
    "https://youtu.be/QzEI9MGRoQw?si=2PvCCZ4mVTh6Kuhi",
    "https://youtu.be/zhW30nCXHmk?si=4SZ9Q-P3yBmX7D5T",
    "https://youtu.be/9ifxakC9Iiw?si=R0MWDNEaLugnUzXn"
]

user_progress = {}
user_quiz_progress = {}

async def handle_c2_1_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c2_1":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c2_1):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c2_1")]
            ])
        )

    elif data == "start_test_c2_1":
        await start_quiz_c2_1(update, context)


async def start_quiz_c2_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c2_1(user_id, query, context)


async def send_quiz_question_c2_1(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c2_1):
        score = progress["score"]
        total = len(quiz_questions_c2_1)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.1", callback_data="start_c2_1")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.1", callback_data="start_c2_1")],
                [InlineKeyboardButton("➡ Բարձրանալ C2.2", callback_data="start_c2_2")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c2_1[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c2_1_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c2_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c2_1_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c2_1[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c2_1(user_id, query, context)
videos_c2_2 = [
    "https://youtu.be/HrOWgg14TUo?si=1ElDdm4pvwqM52Dh",
    "https://youtu.be/c7Nfm5P42KM?si=gDzP-ePYSfpezvqZ",
    "https://youtu.be/8TOgxz0hptM?si=hb-kQEcrScefdWrG"
]

async def handle_c2_2_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c2_2":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c2_2):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c2_2")]
            ])
        )

    elif data == "start_test_c2_2":
        await start_quiz_c2_2(update, context)


async def start_quiz_c2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c2_2(user_id, query, context)


async def send_quiz_question_c2_2(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c2_2):
        score = progress["score"]
        total = len(quiz_questions_c2_2)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.2", callback_data="start_c2_2")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.2", callback_data="start_c2_2")],
                [InlineKeyboardButton("➡ Բարձրանալ C2.3", callback_data="start_c2_3")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c2_2[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c2_2_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c2_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c2_2_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c2_2[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c2_2(user_id, query, context)
videos_c2_3 = [
    "https://youtu.be/-RFjsDlAlNU?si=vbTLWCwAvWNyJoJg",
    "https://youtu.be/63EsmtdOyQo?si=OSoOmJetvKu1P-_j",
    "https://youtu.be/UZsKae1Lkms?si=Xo-1Kc7XG3Tb6HXN"
]

async def handle_c2_3_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c2_3":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c2_3):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c2_3")]
            ])
        )

    elif data == "start_test_c2_3":
        await start_quiz_c2_3(update, context)


async def start_quiz_c2_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c2_3(user_id, query, context)


async def send_quiz_question_c2_3(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c2_3):
        score = progress["score"]
        total = len(quiz_questions_c2_3)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.3", callback_data="start_c2_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.3", callback_data="start_c2_3")],
                [InlineKeyboardButton("➡ Բարձրանալ C2.4", callback_data="start_c2_4")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c2_3[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c2_3_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c2_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c2_3_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c2_3[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c2_3(user_id, query, context)
videos_c2_4 = [
    "https://youtu.be/bS3ZMa1DHm4?si=PlQpGmi-Z8FYVryp",
    "https://youtu.be/PvxF1HbFvr8?si=ZJlO7mcz914Upv1C",
    "https://youtu.be/d_vP1ksSDbI?si=M0F2KTeK2ztVNZ87"
]

async def handle_c2_4_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c2_4":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c2_4):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c2_4")]
            ])
        )

    elif data == "start_test_c2_4":
        await start_quiz_c2_4(update, context)


async def start_quiz_c2_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c2_4(user_id, query, context)


async def send_quiz_question_c2_4(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c2_4):
        score = progress["score"]
        total = len(quiz_questions_c2_4)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.4", callback_data="start_c2_4")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.4", callback_data="start_c2_4")],
                [InlineKeyboardButton("➡ Բարձրանալ C2.5", callback_data="start_c2_5")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c2_4[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c2_4_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c2_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c2_4_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c2_4[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c2_4(user_id, query, context)
videos_c2_5 = [
    "https://youtu.be/wGz0Rys0d2k?si=lCNGcCoaw1teIbHA",
    "https://youtu.be/mDV7z4-5zrI?si=vKEz_Ft7BmQZqmsh",
    "https://youtu.be/0R1R4O7jOT0?si=mqgNIpmKEhNk51KO"
]

async def handle_c2_5_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_c2_5":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ։ Ուշադիր նայեք…")

        for i, video_url in enumerate(videos_c2_5):
            await context.bot.send_message(chat_id=user_id, text=f"Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը։ Եկեք սկսենք թեստը։",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_c2_5")]
            ])
        )

    elif data == "start_test_c2_5":
        await start_quiz_c2_5(update, context)


async def start_quiz_c2_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_c2_5(user_id, query, context)


async def send_quiz_question_c2_5(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_c2_5):
        score = progress["score"]
        total = len(quiz_questions_c2_5)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.5", callback_data="start_c2_5")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել C2.5", callback_data="start_c2_5")],
                [InlineKeyboardButton("Ավարտել Բոտը🎉🥳🎊🎁", callback_data="start_c2_6")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total}-ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_c2_5[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_c2_5_{q_idx}_{i}")] for i, opt in enumerate(options)
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


async def handle_quiz_answer_c2_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ՝ quiz_c2_5_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_c2_5[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_c2_5(user_id, query, context)
