from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from userflow import start, handle_level_selection
from quiz import (
    # A1 Level Handlers (Beginner)
    handle_a1_1_callbacks,
    handle_quiz_answer_a1_1,
    handle_a1_2_callbacks,
    handle_quiz_answer_a1_2,
    handle_a1_3_callbacks,
    handle_quiz_answer_a1_3,
    handle_a1_4_callbacks,
    handle_quiz_answer_a1_4,
    handle_a1_5_callbacks,
    handle_quiz_answer_a1_5,
    handle_a1_6_callbacks,
    handle_quiz_answer_a1_6,
    handle_a1_7_callbacks,
    handle_quiz_answer_a1_7,
    handle_a1_8_callbacks,
    handle_quiz_answer_a1_8,
    handle_a1_9_callbacks,
    handle_quiz_answer_a1_9,
    handle_a1_10_callbacks,
    handle_quiz_answer_a1_10,
    handle_a1_11_callbacks,
    handle_quiz_answer_a1_11,
    handle_a1_12_callbacks,
    handle_quiz_answer_a1_12,
)
from quiz_b1 import (
    # B1 Level Handlers (Intermediate)
    handle_b1_1_callbacks,
    handle_quiz_answer_b1_1,
    handle_b1_2_callbacks,
    handle_quiz_answer_b1_2,
    handle_b1_3_callbacks,
    handle_quiz_answer_b1_3,
    handle_b1_4_callbacks,
    handle_quiz_answer_b1_4,
    handle_b1_5_callbacks,
    handle_quiz_answer_b1_5,
    handle_b1_6_callbacks,
    handle_quiz_answer_b1_6,
    handle_b1_7_callbacks,
    handle_quiz_answer_b1_7,
    handle_b1_8_callbacks,
    handle_quiz_answer_b1_8,
    handle_b1_9_callbacks,
    handle_quiz_answer_b1_9,
    handle_b1_10_callbacks,
    handle_quiz_answer_b1_10,
    handle_b1_11_callbacks,
    handle_quiz_answer_b1_11,
    handle_b1_12_callbacks,
    handle_quiz_answer_b1_12,
)

from quiz_a2 import (
    # A2 Level Handlers (Pre-Intermediate)
    handle_a2_1_callbacks,
    handle_quiz_answer_a2_1,
    handle_a2_2_callbacks,
    handle_quiz_answer_a2_2,
    handle_a2_3_callbacks,
    handle_quiz_answer_a2_3,
    handle_a2_4_callbacks,
    handle_quiz_answer_a2_4,
    handle_a2_5_callbacks,
    handle_quiz_answer_a2_5,
    handle_a2_6_callbacks,
    handle_quiz_answer_a2_6,
    handle_a2_7_callbacks,
    handle_quiz_answer_a2_7,
    handle_a2_8_callbacks,
    handle_quiz_answer_a2_8,
    handle_a2_9_callbacks,
    handle_quiz_answer_a2_9,
    handle_a2_10_callbacks,
    handle_quiz_answer_a2_10,
    handle_a2_11_callbacks,
    handle_quiz_answer_a2_11,
    handle_a2_12_callbacks,
    handle_quiz_answer_a2_12,
)
from quiz_b2 import (
    # B2 Level Handlers (Upper-Intermediate)
    handle_b2_1_callbacks,
    handle_quiz_answer_b2_1,
    handle_b2_2_callbacks,
    handle_quiz_answer_b2_2,
    handle_b2_3_callbacks,
    handle_quiz_answer_b2_3,
    handle_b2_4_callbacks,
    handle_quiz_answer_b2_4,
    handle_b2_5_callbacks,
    handle_quiz_answer_b2_5,
    handle_b2_6_callbacks,
    handle_quiz_answer_b2_6,
    handle_b2_7_callbacks,
    handle_quiz_answer_b2_7,
    handle_b2_8_callbacks,
    handle_quiz_answer_b2_8,
    handle_b2_9_callbacks,
    handle_quiz_answer_b2_9,
    handle_b2_10_callbacks,
    handle_quiz_answer_b2_10,
)
from quiz_c1 import (
    # C1 Level Handlers (Advanced)
    handle_c1_1_callbacks,
    handle_quiz_answer_c1_1,
    handle_c1_2_callbacks,
    handle_quiz_answer_c1_2,
    handle_c1_3_callbacks,
    handle_quiz_answer_c1_3,
    handle_c1_4_callbacks,
    handle_quiz_answer_c1_4,
    handle_c1_5_callbacks,
    handle_quiz_answer_c1_5,
)
from quiz_c2 import (
    # C2 Level Handlers (Proficiency)
    handle_c2_1_callbacks,
    handle_quiz_answer_c2_1,
    handle_c2_2_callbacks,
    handle_quiz_answer_c2_2,
    handle_c2_3_callbacks,
    handle_quiz_answer_c2_3,
    handle_c2_4_callbacks,
    handle_quiz_answer_c2_4,
    handle_c2_5_callbacks,
    handle_quiz_answer_c2_5,
)


BOT_TOKEN = '7789151698:AAF34EiS5FfOZ4-mqgRaNgxAdPLL4zJB6uU'

app = ApplicationBuilder().token(BOT_TOKEN).build()

# Команды
app.add_handler(CommandHandler("start", start))

# Кнопки
# A1 Level Handlers (Beginner)

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(handle_level_selection, pattern="^level:"))

app.add_handler(CallbackQueryHandler(handle_a1_1_callbacks, pattern="^(start_a1_1|start_test_a1_1)$"))
app.add_handler(CallbackQueryHandler(handle_a1_2_callbacks, pattern="^(start_a1_2|start_test2)$"))
app.add_handler(CallbackQueryHandler(handle_a1_3_callbacks, pattern="^(start_a1_3|start_test3)$"))
app.add_handler(CallbackQueryHandler(handle_a1_4_callbacks, pattern="^(start_a1_4|start_test4)$"))
app.add_handler(CallbackQueryHandler(handle_a1_5_callbacks, pattern="^(start_a1_5|start_test5)$"))
app.add_handler(CallbackQueryHandler(handle_a1_6_callbacks, pattern="^(start_a1_6|start_test6)$"))
app.add_handler(CallbackQueryHandler(handle_a1_7_callbacks, pattern="^(start_a1_7|start_test7)$"))
app.add_handler(CallbackQueryHandler(handle_a1_8_callbacks, pattern="^(start_a1_8|start_test8)$"))
app.add_handler(CallbackQueryHandler(handle_a1_9_callbacks, pattern="^(start_a1_9|start_test9)$"))
app.add_handler(CallbackQueryHandler(handle_a1_10_callbacks, pattern="^(start_a1_10|start_test10)$"))
app.add_handler(CallbackQueryHandler(handle_a1_11_callbacks, pattern="^(start_a1_11|start_test11)$"))
app.add_handler(CallbackQueryHandler(handle_a1_12_callbacks, pattern="^(start_a1_12|start_test12)$"))

app.add_handler(CallbackQueryHandler(handle_a2_1_callbacks, pattern="^(start_a2_1|start_test_a2_1)$"))
app.add_handler(CallbackQueryHandler(handle_a2_2_callbacks, pattern="^(start_a2_2|start_test_a2_2)$"))
app.add_handler(CallbackQueryHandler(handle_a2_3_callbacks, pattern="^(start_a2_3|start_test_a2_3)$"))
app.add_handler(CallbackQueryHandler(handle_a2_4_callbacks, pattern="^(start_a2_4|start_test_a2_4)$"))
app.add_handler(CallbackQueryHandler(handle_a2_5_callbacks, pattern="^(start_a2_5|start_test_a2_5)$"))
app.add_handler(CallbackQueryHandler(handle_a2_6_callbacks, pattern="^(start_a2_6|start_test_a2_6)$"))
app.add_handler(CallbackQueryHandler(handle_a2_7_callbacks, pattern="^(start_a2_7|start_test_a2_7)$"))
app.add_handler(CallbackQueryHandler(handle_a2_8_callbacks, pattern="^(start_a2_8|start_test_a2_8)$"))
app.add_handler(CallbackQueryHandler(handle_a2_9_callbacks, pattern="^(start_a2_9|start_test_a2_9)$"))
app.add_handler(CallbackQueryHandler(handle_a2_10_callbacks, pattern="^(start_a2_10|start_test_a2_10)$"))
app.add_handler(CallbackQueryHandler(handle_a2_11_callbacks, pattern="^(start_a2_11|start_test_a2_11)$"))
app.add_handler(CallbackQueryHandler(handle_a2_12_callbacks, pattern="^(start_a2_12|start_test_a2_12)$"))

app.add_handler(CallbackQueryHandler(handle_b1_1_callbacks, pattern="^(start_b1_1|start_test_b1_1)$"))
app.add_handler(CallbackQueryHandler(handle_b1_2_callbacks, pattern="^(start_b1_2|start_test_b1_2)$"))
app.add_handler(CallbackQueryHandler(handle_b1_3_callbacks, pattern="^(start_b1_3|start_test_b1_3)$"))
app.add_handler(CallbackQueryHandler(handle_b1_4_callbacks, pattern="^(start_b1_4|start_test_b1_4)$"))
app.add_handler(CallbackQueryHandler(handle_b1_5_callbacks, pattern="^(start_b1_5|start_test_b1_5)$"))
app.add_handler(CallbackQueryHandler(handle_b1_6_callbacks, pattern="^(start_b1_6|start_test_b1_6)$"))
app.add_handler(CallbackQueryHandler(handle_b1_7_callbacks, pattern="^(start_b1_7|start_test_b1_7)$"))
app.add_handler(CallbackQueryHandler(handle_b1_8_callbacks, pattern="^(start_b1_8|start_test_b1_8)$"))
app.add_handler(CallbackQueryHandler(handle_b1_9_callbacks, pattern="^(start_b1_9|start_test_b1_9)$"))
app.add_handler(CallbackQueryHandler(handle_b1_10_callbacks, pattern="^(start_b1_10|start_test_b1_10)$"))
app.add_handler(CallbackQueryHandler(handle_b1_11_callbacks, pattern="^(start_b1_11|start_test_b1_11)$"))
app.add_handler(CallbackQueryHandler(handle_b1_12_callbacks, pattern="^(start_b1_12|start_test_b1_12)$"))

app.add_handler(CallbackQueryHandler(handle_b2_1_callbacks, pattern="^(start_b2_1|start_test_b2_1)$"))
app.add_handler(CallbackQueryHandler(handle_b2_2_callbacks, pattern="^(start_b2_2|start_test_b2_2)$"))
app.add_handler(CallbackQueryHandler(handle_b2_3_callbacks, pattern="^(start_b2_3|start_test_b2_3)$"))
app.add_handler(CallbackQueryHandler(handle_b2_4_callbacks, pattern="^(start_b2_4|start_test_b2_4)$"))
app.add_handler(CallbackQueryHandler(handle_b2_5_callbacks, pattern="^(start_b2_5|start_test_b2_5)$"))
app.add_handler(CallbackQueryHandler(handle_b2_6_callbacks, pattern="^(start_b2_6|start_test_b2_6)$"))
app.add_handler(CallbackQueryHandler(handle_b2_7_callbacks, pattern="^(start_b2_7|start_test_b2_7)$"))
app.add_handler(CallbackQueryHandler(handle_b2_8_callbacks, pattern="^(start_b2_8|start_test_b2_8)$"))
app.add_handler(CallbackQueryHandler(handle_b2_9_callbacks, pattern="^(start_b2_9|start_test_b2_9)$"))
app.add_handler(CallbackQueryHandler(handle_b2_10_callbacks, pattern="^(start_b2_10|start_test_b2_10)$"))

app.add_handler(CallbackQueryHandler(handle_c1_1_callbacks, pattern="^(start_c1_1|start_test_c1_1)$"))
app.add_handler(CallbackQueryHandler(handle_c1_2_callbacks, pattern="^(start_c1_2|start_test_c1_2)$"))
app.add_handler(CallbackQueryHandler(handle_c1_3_callbacks, pattern="^(start_c1_3|start_test_c1_3)$"))
app.add_handler(CallbackQueryHandler(handle_c1_4_callbacks, pattern="^(start_c1_4|start_test_c1_4)$"))
app.add_handler(CallbackQueryHandler(handle_c1_5_callbacks, pattern="^(start_c1_5|start_test_c1_5)$"))

app.add_handler(CallbackQueryHandler(handle_c2_1_callbacks, pattern="^(start_c2_1|start_test_c2_1)$"))
app.add_handler(CallbackQueryHandler(handle_c2_2_callbacks, pattern="^(start_c2_2|start_test_c2_2)$"))
app.add_handler(CallbackQueryHandler(handle_c2_3_callbacks, pattern="^(start_c2_3|start_test_c2_3)$"))
app.add_handler(CallbackQueryHandler(handle_c2_4_callbacks, pattern="^(start_c2_4|start_test_c2_4)$"))
app.add_handler(CallbackQueryHandler(handle_c2_5_callbacks, pattern="^(start_c2_5|start_test_c2_5)$"))


# A1 Level Answer Handlers (Beginner)
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_1, pattern=r"^quiz_a1_1_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_2, pattern=r"^quiz_a1_2_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_3, pattern=r"^quiz_a1_3_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_4, pattern=r"^quiz_a1_4_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_5, pattern=r"^quiz_a1_5_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_6, pattern=r"^quiz_a1_6_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_7, pattern=r"^quiz_a1_7_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_8, pattern=r"^quiz_a1_8_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_9, pattern=r"^quiz_a1_9_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_10, pattern=r"^quiz_a1_10_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_11, pattern=r"^quiz_a1_11_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a1_12, pattern=r"^quiz_a1_12_\d+_\d+$"))

app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_1, pattern=r"^quiz_a2_1_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_2, pattern=r"^quiz_a2_2_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_3, pattern=r"^quiz_a2_3_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_4, pattern=r"^quiz_a2_4_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_5, pattern=r"^quiz_a2_5_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_6, pattern=r"^quiz_a2_6_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_7, pattern=r"^quiz_a2_7_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_8, pattern=r"^quiz_a2_8_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_9, pattern=r"^quiz_a2_9_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_10, pattern=r"^quiz_a2_10_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_11, pattern=r"^quiz_a2_11_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_a2_12, pattern=r"^quiz_a2_12_\d+_\d+$"))

app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_1, pattern=r"^quiz_b1_1_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_2, pattern=r"^quiz_b1_2_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_3, pattern=r"^quiz_b1_3_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_4, pattern=r"^quiz_b1_4_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_5, pattern=r"^quiz_b1_5_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_6, pattern=r"^quiz_b1_6_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_7, pattern=r"^quiz_b1_7_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_8, pattern=r"^quiz_b1_8_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_9, pattern=r"^quiz_b1_9_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_10, pattern=r"^quiz_b1_10_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_11, pattern=r"^quiz_b1_11_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b1_12, pattern=r"^quiz_b1_12_\d+_\d+$"))

app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_1, pattern=r"^quiz_b2_1_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_2, pattern=r"^quiz_b2_2_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_3, pattern=r"^quiz_b2_3_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_4, pattern=r"^quiz_b2_4_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_5, pattern=r"^quiz_b2_5_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_6, pattern=r"^quiz_b2_6_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_7, pattern=r"^quiz_b2_7_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_8, pattern=r"^quiz_b2_8_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_9, pattern=r"^quiz_b2_9_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_b2_10, pattern=r"^quiz_b2_10_\d+_\d+$"))

app.add_handler(CallbackQueryHandler(handle_quiz_answer_c1_1, pattern=r"^quiz_c1_1_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c1_2, pattern=r"^quiz_c1_2_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c1_3, pattern=r"^quiz_c1_3_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c1_4, pattern=r"^quiz_c1_4_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c1_5, pattern=r"^quiz_c1_5_\d+_\d+$"))

app.add_handler(CallbackQueryHandler(handle_quiz_answer_c2_1, pattern=r"^quiz_c2_1_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c2_2, pattern=r"^quiz_c2_2_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c2_3, pattern=r"^quiz_c2_3_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c2_4, pattern=r"^quiz_c2_4_\d+_\d+$"))
app.add_handler(CallbackQueryHandler(handle_quiz_answer_c2_5, pattern=r"^quiz_c2_5_\d+_\d+$"))


print("Бот запущен!")
app.run_polling()
