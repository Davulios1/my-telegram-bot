from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
import asyncio
from data.questions import (
    quiz_questions_b1_1,
    quiz_questions_b1_2,
    quiz_questions_b1_3,
    quiz_questions_b1_4,
    quiz_questions_b1_5,
    quiz_questions_b1_6,
    quiz_questions_b1_7,
    quiz_questions_b1_8,
    quiz_questions_b1_9,
    quiz_questions_b1_10,
    quiz_questions_b1_11,
    quiz_questions_b1_12
)

videos_b1_1 = [
    "https://youtu.be/d0WHPe34o4M?si=xrrfUvBE-Yxn-e_2",
    "https://youtu.be/R1n6IF3ViQY?si=41I21DfSplqbNGMz",
    "https://www.youtube.com/live/mnE_u80P-PQ?si=r9xOvwKOMMcxRzqE"
]

user_progress = {}
user_quiz_progress = {}

async def handle_b1_1_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_1":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_1):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_1")]
            ])
        )

    elif data == "start_test_b1_1":
        await start_quiz_b1_1(update, context)


async def start_quiz_b1_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_1(user_id, query, context)


async def send_quiz_question_b1_1(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_1):
        score = progress["score"]
        total = len(quiz_questions_b1_1)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.1", callback_data="start_b1_1")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.1", callback_data="start_b1_1")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.2", callback_data="start_b1_2")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_1[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_1_{q_idx}_{i}")]
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

async def handle_quiz_answer_b1_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_1_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_1[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_1(user_id, query, context)

videos_b1_2 = [
    "https://www.youtube.com/live/cI4NIb4h9ZE?si=sy4HUma8Elx8sWNo",
    "https://www.youtube.com/live/nMMsujzjuj0?si=1g2nJgzV4Cwvt3MA",
    "https://www.youtube.com/live/_QwAG_lKqyE?si=wJzPf9Fq8brdLpIL"
]

async def handle_b1_2_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_2":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_2):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_2")]
            ])
        )

    elif data == "start_test_b1_2":
        await start_quiz_b1_2(update, context)


async def start_quiz_b1_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_2(user_id, query, context)


async def send_quiz_question_b1_2(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_2):
        score = progress["score"]
        total = len(quiz_questions_b1_2)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.2", callback_data="start_b1_2")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.2", callback_data="start_b1_2")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.3", callback_data="start_b1_3")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_2[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_2_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_2_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_2[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_2(user_id, query, context)

videos_b1_3 = [
    "https://www.youtube.com/live/PN_2p7B2RqU?si=CQC16YcXOP4J3sSQ",
    "https://www.youtube.com/live/I_Bw0wWUvGc?si=eRVVzykNMcx5PDyV",
    "https://www.youtube.com/live/DS6qVlFiAuc?si=oVSZs7ahpYcJOxc0"
]

async def handle_b1_3_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_3":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_3):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_3")]
            ])
        )

    elif data == "start_test_b1_3":
        await start_quiz_b1_3(update, context)


async def start_quiz_b1_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_3(user_id, query, context)


async def send_quiz_question_b1_3(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_3):
        score = progress["score"]
        total = len(quiz_questions_b1_3)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.3", callback_data="start_b1_3")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.3", callback_data="start_b1_3")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.4", callback_data="start_b1_4")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_3[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_3_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_3_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_3[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_3(user_id, query, context)

videos_b1_4 = [
    "https://www.youtube.com/live/X7eNaJLwXe8?si=jAPcOUe1sHZ_eerp",
    "https://www.youtube.com/live/3bamePxfxWM?si=Fj4il1A09es6av7M",
    "https://www.youtube.com/live/SYOwg2JX6T8?si=2tjNLq4lVht-7MA8"
]

async def handle_b1_4_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_4":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_4):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_4")]
            ])
        )

    elif data == "start_test_b1_4":
        await start_quiz_b1_4(update, context)


async def start_quiz_b1_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_4(user_id, query, context)


async def send_quiz_question_b1_4(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_4):
        score = progress["score"]
        total = len(quiz_questions_b1_4)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.4", callback_data="start_b1_4")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.4", callback_data="start_b1_4")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.5", callback_data="start_b1_5")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_4[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_4_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_4(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_4_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_4[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_4(user_id, query, context)
videos_b1_5 = [
    "https://www.youtube.com/live/Tk60ucAMnyE?si=x8bdRwvkl9XMXAyA",
    "https://www.youtube.com/live/kurgC_KVECk?si=oflu7nRoxk-Kgdjv",
    "https://youtu.be/Ucu3a5R6ZXg?si=0B-45A4mF5W2H58s"
]

async def handle_b1_5_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_5":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_5):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_5")]
            ])
        )

    elif data == "start_test_b1_5":
        await start_quiz_b1_5(update, context)


async def start_quiz_b1_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_5(user_id, query, context)


async def send_quiz_question_b1_5(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_5):
        score = progress["score"]
        total = len(quiz_questions_b1_5)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.5", callback_data="start_b1_5")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.5", callback_data="start_b1_5")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.6", callback_data="start_b1_6")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_5[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_5_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_5(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_5_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_5[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_5(user_id, query, context)
videos_b1_6 = [
    "https://www.youtube.com/live/I_Bw0wWUvGc?si=uWr4NLaoZDUL6xRP",
    "https://www.youtube.com/live/DS6qVlFiAuc?si=49RNFq3s3hxQWlCE",
    "https://www.youtube.com/live/tPXKiGhX1hw?si=rptPxr2w0aohsclF"
]

async def handle_b1_6_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_6":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_6):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_6")]
            ])
        )

    elif data == "start_test_b1_6":
        await start_quiz_b1_6(update, context)


async def start_quiz_b1_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_6(user_id, query, context)


async def send_quiz_question_b1_6(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_6):
        score = progress["score"]
        total = len(quiz_questions_b1_6)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.6", callback_data="start_b1_6")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.6", callback_data="start_b1_6")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.7", callback_data="start_b1_7")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_6[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_6_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_6(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_6_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_6[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_6(user_id, query, context)

videos_b1_7 = [
    "https://www.youtube.com/live/XEwN3BjR7lk?si=Dcbamx2n5ibLfeJK",
    "https://www.youtube.com/live/3bamePxfxWM?si=MEc89RXR-E6d-G0v",
    "https://www.youtube.com/live/f6osQlbj0RA?si=rV-6JeJFXbOjSyoa"
]

async def handle_b1_7_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_7":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_7):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_7")]
            ])
        )

    elif data == "start_test_b1_7":
        await start_quiz_b1_7(update, context)
async def start_quiz_b1_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_7(user_id, query, context)


async def send_quiz_question_b1_7(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_7):
        score = progress["score"]
        total = len(quiz_questions_b1_7)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.7", callback_data="start_b1_7")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.7", callback_data="start_b1_7")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.8", callback_data="start_b1_8")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_7[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_7_{q_idx}_{i}")]
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
async def handle_quiz_answer_b1_7(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_7_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_7[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_7(user_id, query, context)
videos_b1_8 = [
    "https://www.youtube.com/live/EvFqPjIJFJk?si=ulhkeNOR9C64i-QQ",
    "https://www.youtube.com/live/X7eNaJLwXe8?si=-0-Vhquj6EmDXFus",
    "https://www.youtube.com/live/CKRaUuMhL8s?si=U0aztznVx9nWmXwB"
]

async def handle_b1_8_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_8":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_8):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_8")]
            ])
        )

    elif data == "start_test_b1_8":
        await start_quiz_b1_8(update, context)
async def start_quiz_b1_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_8(user_id, query, context)


async def send_quiz_question_b1_8(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_8):
        score = progress["score"]
        total = len(quiz_questions_b1_8)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.8", callback_data="start_b1_8")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.8", callback_data="start_b1_8")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.9", callback_data="start_b1_9")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_8[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_8_{q_idx}_{i}")]
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
async def handle_quiz_answer_b1_8(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_8_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_8[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_8(user_id, query, context)
videos_b1_9 = [
    "https://youtu.be/R1n6IF3ViQY?si=jiLLU4GqFXPyDhZi",
    "https://youtu.be/d0WHPe34o4M?si=NGnc4OwXSFMkPi0i",
    "https://youtu.be/Ip5UN4xDR_Y?si=dKjZ-xIjvBEsgdgi"
]

async def handle_b1_9_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_9":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_9):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_9")]
            ])
        )

    elif data == "start_test_b1_9":
        await start_quiz_b1_9(update, context)
async def start_quiz_b1_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }
    await send_quiz_question_b1_9(user_id, query, context)


async def send_quiz_question_b1_9(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_9):
        score = progress["score"]
        total = len(quiz_questions_b1_9)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.9", callback_data="start_b1_9")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.9", callback_data="start_b1_9")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.10", callback_data="start_b1_10")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_9[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_9_{q_idx}_{i}")]
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
async def handle_quiz_answer_b1_9(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_9_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_9[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_9(user_id, query, context)

videos_b1_10 = [
    "https://youtu.be/17CtvQeCOKI?si=Ly_bZZX-CSR5tIPi",
    "https://youtu.be/tOUI9_deTjE?si=a2q0h4sssM44lMVd",
    "https://youtu.be/Y0XhuITT70o?si=LcP0cD5qgV9z-zCs"
]

async def handle_b1_10_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_10":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_10):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_10")]
            ])
        )

    elif data == "start_test_b1_10":
        await start_quiz_b1_10(update, context)


async def start_quiz_b1_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_10(user_id, query, context)


async def send_quiz_question_b1_10(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_10):
        score = progress["score"]
        total = len(quiz_questions_b1_10)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.10", callback_data="start_b1_10")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.10", callback_data="start_b1_10")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.11", callback_data="start_b1_11")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_10[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_10_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_10(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_10_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_10[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_10(user_id, query, context)


videos_b1_11 = [
    "https://youtu.be/J6EO4CrTLBk?si=O_bIthwCVAHmzh_s",
    "https://youtu.be/_-9VMrLOEfo?si=TP7vi49fFwR5txpa",
    "https://youtu.be/_k5ZL0VBUNY?si=eiQnuwXV4VR2WhlY"
]

async def handle_b1_11_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_11":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_11):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_11")]
            ])
        )

    elif data == "start_test_b1_11":
        await start_quiz_b1_11(update, context)


async def start_quiz_b1_11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_11(user_id, query, context)


async def send_quiz_question_b1_11(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_11):
        score = progress["score"]
        total = len(quiz_questions_b1_11)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.11", callback_data="start_b1_11")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.11", callback_data="start_b1_11")],
                [InlineKeyboardButton("➡ Բարձրանալ B1.12", callback_data="start_b1_12")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_11[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_11_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_11(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_11_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_11[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_11(user_id, query, context)
videos_b1_12 = [
    "https://youtu.be/ylKfQp4WESY?si=qLM0tnnRgvIjNRyw",
    "https://youtu.be/ld0cp2aZ0rQ?si=C8GHZ-nzfK2pJiyi",
    "https://youtu.be/o3ZUMvh1Uow?si=5os1k2NV7ZbLcyLp"
]

async def handle_b1_12_callbacks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id
    data = query.data

    if data == "start_b1_12":
        user_progress[user_id] = {"video_sent": True}
        await query.edit_message_text("🎬 Այժմ դուք կստանաք 3 տեսանյութ: Ուշադիր նայեք...")

        for i, video_url in enumerate(videos_b1_12):
            await context.bot.send_message(chat_id=user_id, text=f"Դիտեք առնվազն 20 վայրկյան: Տեսանյութ {i+1}:\n{video_url}")
            await asyncio.sleep(2)

        await context.bot.send_message(
            chat_id=user_id,
            text="Դիտեցի՞ք բոլոր 3 տեսանյութերը: Եկեք սկսենք թեստը!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Սկսել թեստը", callback_data="start_test_b1_12")]
            ])
        )

    elif data == "start_test_b1_12":
        await start_quiz_b1_12(update, context)


async def start_quiz_b1_12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    user_quiz_progress[user_id] = {
        "current_question": 0,
        "score": 0
    }

    await send_quiz_question_b1_12(user_id, query, context)


async def send_quiz_question_b1_12(user_id, query, context):
    progress = user_quiz_progress[user_id]
    q_idx = progress["current_question"]

    if q_idx >= len(quiz_questions_b1_12):
        score = progress["score"]
        total = len(quiz_questions_b1_12)

        if score < 8:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.12", callback_data="start_b1_12")]
            ]
        else:
            keyboard = [
                [InlineKeyboardButton("🔁 Կրկնել B1.12", callback_data="start_b1_12")],
                [InlineKeyboardButton("➡ Բարձրանալ B2.1", callback_data="start_b2_1")]
            ]

        await context.bot.send_message(
            chat_id=user_id,
            text=f"✅ Թեստն ավարտված է։\nՁեր արդյունքը՝ {score} միավոր {total} -ից։",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    question = quiz_questions_b1_12[q_idx]
    options = question["options"]

    keyboard = [
        [InlineKeyboardButton(opt, callback_data=f"quiz_b1_12_{q_idx}_{i}")]
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


async def handle_quiz_answer_b1_12(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    data = query.data  # օրինակ: quiz_b1_12_0_2
    parts = data.split("_")
    if len(parts) != 5:
        return

    q_idx = int(parts[3])
    selected_option = int(parts[4])

    progress = user_quiz_progress.get(user_id)
    if not progress or progress["current_question"] != q_idx:
        return

    question = quiz_questions_b1_12[q_idx]
    if selected_option == question["correct"]:
        progress["score"] += 1

    progress["current_question"] += 1
    await send_quiz_question_b1_12(user_id, query, context)
