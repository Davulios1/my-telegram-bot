import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Օգտատերերի պահոց
users = {}

# Անգլերենի մակարդակները
levels = {
    "A1": "Սկսնակ",
    "A2": "Տարրական",
    "B1": "Միջին",
    "B2": "Միջինից բարձր",
    "C1": "Ընդլայնված",
    "C2": "Պրոֆեսիոնալ"
}

# Ալիքների հղումներ
telegram_channel_url = "https://t.me/LearnLanguagesWithDiana"
telegram_channel_username = "https://www.youtube.com/@dlearnenglish"  # առանց @
youtube_channel_url = "https://www.youtube.com/@dlearnenglish"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.first_name

    if user_id not in users:
        users[user_id] = {
            "name": username,
            "score": 0,
            "level": None
        }
        subscribe_text = (
            f"Ողջույն, {username}! Նախքան սկսելը, խնդրում ենք բաժանորդագրվել մեր ալիքներին:\n\n"
            f"👉 Telegram ալիք: @{telegram_channel_username}\n"
            f"👉 YouTube ալիք: {youtube_channel_url}\n\n"
            "Բաժանորդագրությունից հետո մակարդակների ընտրացանկը կհայտնվի 10 վայրկյանից:"
        )
        keyboard = [
            [
                InlineKeyboardButton("Բաժանորդագրվել Telegram-ին", url=telegram_channel_url),
                InlineKeyboardButton("Բաժանորդագրվել YouTube-ին", url=youtube_channel_url)
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await update.message.reply_text(subscribe_text, reply_markup=reply_markup)

        await asyncio.sleep(30)
        await show_level_menu_after_subscribe(sent_message)
    else:
        await update.message.reply_text(f"Բարի վերադարձ, {username} 🫡")
        await show_level_menu(update)

async def show_level_menu_after_subscribe(message):
    keyboard = [
        [InlineKeyboardButton(f"{key} – {value}", callback_data=f"level:{key}")]
        for key, value in levels.items()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.edit_text("Ընտրիր անգլերենի քո մակարդակը:", reply_markup=reply_markup)

async def show_level_menu(update: Update):
    keyboard = [
        [InlineKeyboardButton(f"{key} – {value}", callback_data=f"level:{key}")]
        for key, value in levels.items()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Ընտրիր անգլերենի քո մակարդակը:", reply_markup=reply_markup)

async def handle_level_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    data = query.data

    if data.startswith("level:"):
        level_code = data.split(":")[1]
        users[user_id]["level"] = level_code
        level_name = levels[level_code]

        if level_code == "A1":
            await query.edit_message_text(
                f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}\n\n"
                "🎮 Բարի գալուստ A1.1 մակարդակ:\n"
                "📺 Սկզբում դու դիտում ես 3 կարճ ուսումնական տեսանյութ YouTube-ից:\n"
                "🧠 Դիտումից հետո անցնում ես թեստ՝ ստուգելու քո հասկանալը:\n"
                "🏆 Անցնելու համար անհրաժեշտ է հավաքել առնվազն 11 միավոր 13-ից:\n\n"
                "Սեղմիր «Սկսել A1.1 մակարդակը»՝ սկսելու համար։",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Սկսել A1.1 մակարդակը", callback_data="start_a1_1")]
                ])
            )

        elif level_code == "A2":
            await query.edit_message_text(
                f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}\n\n"
                "🎮 Բարի գալուստ A2.1 մակարդակ:\n"
                "📺 Սկզբում դիտում ես 3 նոր տեսանյութ:\n"
                "🧠 Այնուհետեւ անցնում ես թեստ՝ քո գիտելիքները ստուգելու համար:\n"
                "🏆 Անցնելու համար պետք է ճիշտ պատասխանել առնվազն 8 հարցի:\n\n"
                "Սեղմիր «Սկսել A2.1 մակարդակը»՝ սկսելու համար։",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Սկսել A2.1 մակարդակը", callback_data="start_a2_1")]
                ])
            )

        elif level_code == "B1":
            await query.edit_message_text(
                f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}\n\n"
                "🎮 Բարի գալուստ B1.1 մակարդակ:\n"
                "📺 Դիտում ես 3 տեսանյութ միջին մակարդակի համար:\n"
                "🧠 Այնուհետեւ անցնում ես թեստ՝ քո գիտելիքները ստուգելու համար:\n"
                "🏆 Անցնելու համար պետք է ճիշտ պատասխանել առնվազն 8 հարցի:\n\n"
                "Սեղմիր «Սկսել B1.1 մակարդակը»՝ սկսելու համար։",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Սկսել B1.1 մակարդակը", callback_data="start_b1_1")]
                ])
            )
        elif level_code == "B2":
            await query.edit_message_text(
                f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}\n\n"
                "🎮 Բարի գալուստ B2.1 մակարդակ:\n"
                "📺 Դիտում ես 3 տեսանյութ՝ ավելի բարդ բառապաշարով ու կառուցվածքներով:\n"
                "🧠 Այնուհետեւ անցնում ես թեստ՝ քո գիտելիքները ստուգելու համար:\n"
                "🏆 Անցնելու համար պետք է ճիշտ պատասխանել առնվազն 9 հարցի:\n\n"
                "Սեղմիր «Սկսել B2.1 մակարդակը»՝ սկսելու համար։",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Սկսել B2.1 մակարդակը", callback_data="start_b2_1")]
                ])
            )

        elif level_code == "C1":
            await query.edit_message_text(
                f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}\n\n"
                "🎮 Բարի գալուստ C1.1 մակարդակ:\n"
                "📺 Դիտում ես 3 տեսանյութ՝ ակադեմիական և պաշտոնական լեզվով:\n"
                "🧠 Այնուհետեւ անցնում ես թեստ՝ քո խորացված գիտելիքները ստուգելու համար:\n"
                "🏆 Անցնելու համար պետք է ճիշտ պատասխանել առնվազն 10 հարցի:\n\n"
                "Սեղմիր «Սկսել C1.1 մակարդակը»՝ սկսելու համար։",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Սկսել C1.1 մակարդակը", callback_data="start_c1_1")]
                ])
            )

        elif level_code == "C2":
            await query.edit_message_text(
                f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}\n\n"
                "🎮 Բարի գալուստ C2.1 մակարդակ:\n"
                "📺 Դիտում ես 3 տեսանյութ՝ մերձմայրենի խոսքի մակարդակով:\n"
                "🧠 Այնուհետեւ անցնում ես թեստ՝ քո վերլուծական ու լեզվաբանական ունակությունները ստուգելու համար:\n"
                "🏆 Անցնելու համար պետք է ճիշտ պատասխանել բոլոր 10 հարցերին:\n\n"
                "Սեղմիր «Սկսել C2.1 մակարդակը»՝ սկսելու համար։",
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton("Սկսել C2.1 մակարդակը", callback_data="start_c2_1")]
                ])
            )

        else:
            await query.edit_message_text(f"✅ Մակարդակը սահմանված է: {level_code} – {level_name}")
