from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

################################
## Dev By: @WWWL5 & @MRv7x ##
################################

@Client.on_callback_query(filters.regex("^command (\\d+)$"))
async def command(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(m.from_user.id))],

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],

    ])
    await m.reply_text("""
♡اوامــر البــوت الرئيسيـة 
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸𝐽𝐴𝐶𝐾━━━━●
♡{ م1 } ← اوامر الحمايه
♡{ م2 } ← اوامر التسليه
♡{ م3 } ← اوامر الاعضاء
♡{ م4 } ← اوامر الرتب
♡{ م5 } ← اوامر الموسيقئ
♡{ م6 } ← اوامر المطورين
♡{ م المطور } ← اوامر المطور

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^command2 (\\d+)$"))
async def command2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⨳ م1", callback_data="m1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م2", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م3", callback_data="m3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م4", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("⨳ م5", callback_data="m5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⨳ م6", callback_data="m6 " + str(m.from_user.id))],

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],

    ])
    await m.message.edit_text("""
♡اوامــر البــوت الرئيسيـة 
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
♡{ م1 } ← اوامر الحمايه
♡{ م2 } ← اوامر التسليه
♡{ م3 } ← اوامر الاعضاء
♡{ م4 } ← اوامر الرتب
♡{ م5 } ← اوامر الموسيقئ
♡{ م6 } ← اوامر المطورين
♡{ م المطور } ← اوامر المطور

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m1 (\\d+)$"))
async def m1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⚙️⁩ ❬ م1 ❭ اوامر حماية المجموعه ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🔐 ╖ قفل «» فتح + الامر 
⁦♻️⁩ ╜ قفل «» فتح ❬ الكـــل ❭ 
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
📮╖ الدردشه
📜╢ المعرفات
📸╢ الصور
📽️╢ الفيديوهات
🎟╢ الاستيكر
📂╢ الملفات
🎥╢ المتحركه
⏏️╢ الرفع
🔊╢ الريكورد
🎧╢ الصوت
📞╢ الجهات
🔊╢ الترحيب
🚫╢ المغادره
🎧╢ الاغاني
🏨╢ الزخرفه
🍿╢ الافلام
🎬╢ اليوتيوب
💱╢ الترجمه
🔄╢ الردود
🚿╢ التوجيه
🗳️╢ الاشعارات
💳╢ التاج
🧾╢ رابط الحذف
🔈╢ اطردني
🤔╢ مين ضافني
🏓╢ الالعاب
🎁╢ الروايات
🎆╢ الابراج
🔍╢ معاني الاسماء
💬╜ الترحيب
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
⚠️ ❬ بالكتم, بالطرد ❭
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🌐╖ الروابط
🔄╢ التوجيه
🍿╢ الفشار
⚜️╢ البوتات
⚠️╜ الممنوعه
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mxx (\\d+)$"))
async def mxx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m2 (\\d+)$"))
async def m2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("اوامر التسليه 1⃣", callback_data="mx1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("اوامر التسليه 2⃣", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text(" ◍ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^mx1 (\\d+)$"))
async def mx1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("➡️ التالي", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 1⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🐣╖ متوحد «» متوحده
💬╢ تاج للمتوحدين 
📎╜ مسح المتوحدين
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
💢╖ بقره 
💬╢ تاج للبقرات
📎╜ مسح البقرات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🐒╖ غبي
💬╢ تاج للاغبيه
📎╜ مسح الاغبيه
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🤪╖ حمار
💬╢ تاج للحمير
📎╜ مسح الحمير
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🤡╖ فرسه
💬╢ تاج للفرسات
📎╜ مسح الفرسات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🤰╖ عره
💬╢ تاج للعرر
📎╜ مسح العرر
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
👰╖ زوجتي
💬╢ تاج للزوجات
📎╜ مسح المتزوجات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
👩‍❤️‍👨╖ زواج «» طلاق
💬╢ تاج للمتزوجين 
📎╜ مسح المتزوجين
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
💘╖ رفع بقلبي «» تنزيل من قلبي
💬╢ تاج للي بقلبي
📎╜ مسح من قلبي
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🙊╖ بيستي 
💬╢ تاج للبيست
📎╜ مسح البيستيه
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●

    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mx2 (\\d+)$"))
async def mx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""🥳╖ ❬ م2 ❭ 2⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🐣╖ وتكه
💬╢ تاج للوتكات 
📎╜ مسح الوتكات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
💢╖ رقاصه 
💬╢ تاج للرقاصات
📎╜ مسح الرقاصات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🐒╖ مهزء
💬╢ تاج للمهزئين
📎╜ مسح المهزئين
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🤪╖ حيوان
💬╢ تاج للحيوانات
📎╜ الحيوانات 
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🐕╖ فاشل
💬╢ تاج للفشله
📎╜ مسح الفشله
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🐰╖ دكري
💬╢ تاج للدكور
📎╜ مسح الدكور
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🤡╖ قطتي
💬╢ تاج للقطط
📎╜ مسح القطط
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🤰╖ ابني
💬╢ تاج للابناء
📎╜ مسح الابناء
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
👰╖ بنتي
💬╢ تاج للبنوتات
📎╜ مسح البنوتات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
👩‍❤️‍👨╖ حبيبي
💬╢ تاج للحبايب 
📎╜ مسح الحبايب
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
💘╖ زوجي
💬╢ تاج للازواج
📎╜ مسح الازواج
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🙊╖ زوجتي 
💬╢ تاج للزوجات
📎╜ مسح الزوجات
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
👰╖ خاين
💬╢ تاج للخونه
📎╜ مسح الخونه
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
👩‍❤️‍👨╖ خاينه
💬╢ تاج للخاينين 
📎╜ مسح الخاينين
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
💘╖ عبيط
💬╢ تاج للعبط
📎╜ مسح العبط
●━━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━━●
🙊╖ متخزوق 
💬╢ تاج للمتخزوقين
📎╜ مسح المتخزوقين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·

    """, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m3 (\\d+)$"))
async def m3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
💫 ❬ م3 ❭ اوامر الاعضاء ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🎤╖ غنيلي «» حساب العمر
🖼️╢ صورتي «» نسبه جمالي
📖╢ قرءان
⚙️╢ الاعدادات
🔘╢ نقاطي
⚜️╢ حذف «» بيع ❬ نقاطي ❭
💌╢ رسائلي «» حذف ❬ رسائلي ❭
🔊╢ زخرفه «» اغاني 
🎥╢ افلام «» كارتون
🧭╢ ترجمه + روايات
📼╢ يوتيوب «» العاب
🌡╢ طقس + المنطقة 
🦞╢ فينوم «» الرابط
🥱╢ اسمي «» الرتبه
💞╢ بحبك «» تتجوزيني
⚕️╢ جهاتي «» حذف جهاتي
☣️╢ صلاحياتي «» بينج
🔉╢ قول + الكلمه
⛔️╢ الكلمات الممنوعه
⭐️╢ انا مين «» انا فين
♻️╢ قول + الكلمه
🐕╢ قطه «» كلب 
💔╢ اطردني «» اكتمني
🌐╢ تاك للاونلاين «» تاك للاعضاء
👨‍🏫╢ سورس «» المطور
♋️╢ الرابط «» ايدي
⬆️╢ رتبتي «» كشف
📊╢ رد  انت يا بوت
🤔╢ اي رايك يابوت
😈╢ هينو «» هينها
💋╢ بوسو «» بوسها
🙊╢ بتحب دي «» بتحب ده
🌀╢ اسامة «»  فينوم
⚠️╜ رابط الحذف
═══════『𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾』═══════ٴ
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m4 (\\d+)$"))
async def m4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
👮‍♂️╖ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
⚠️╜ الادمن «» المنشئ «» المالك
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🥳 « المميز » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🙈╖ كشف
🔇╢ المحظورين
🔕╢ المكتومين
🍿╜ بس كده 😹💔
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🐣 « الادمن » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🥳╖ رفع مميز «» تنزيل مميز
🙋╢ الترحيب
🤬╢ اضف مغادره «» مسح المغادره
🚫╢ رساله المغادره
🤖╢ كشف البوتات
🥳╢ المميزين «» حذف المميزين
🛡╢ حظر «» الغاء حظر
🗡╢ كتم «» الغاء كتم
🗑╢ حظر لمده + المده
🧺╢ كتم لمده + المده
😠╢ طرد «» تطهير 
📌╢ تثبيت «» تثبيت بدون اشعار
🧷╢ الغاء تثبيت الكل
📚╜ ❬ + ❭ جميع ماسبق
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🤵 « المنشئ » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🐣╖ رفع «» تنزيل ادمن
💌╢ اضف «» حذف  ❬ رد ❭
👨‍🎨╢ الردود «» حذف الردود
🔕╢ ايقاف المنشن
💫╢ تعيين «» مسح  ❬ الايدي ❭
👨‍✈️╢ الادمنيه «» حذف الادمنيه
🍻╢ اضف ترحيب
🎲╢ حذف المحظورين «» المكتومين
🎯╢ منع + الكلمه
🚜╢ الغاء منع + الكلمه
🚨╢ حذف الكلمات الممنوعه
🔍╢ المميزين عام
📚╜ ❬ + ❭ جميع ماسبق
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
👮‍♂️ « المالك » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🔼╖ اضف صوره «» وصف (للجروب)
🤵╢ رفع منشئ «» تنزيل منشئ
🔊╢ تاج للاعضاء «» للكل
🔗╢ اضف رابط «» مسح الرابط
🔖╢ اضف «» حذف  ❬ امر ❭
📝╢ الاوامر المضافه
🗑╢ حذف الاوامر المضافه
🔏╢ اضف اسم «» تحديث
🍿╢ المنشئين «» حذف المنشئين
📚╜ ❬ + ❭ جميع ماسبق
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m5 (\\d+)$"))
async def m5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
🎵╖ ❬ م5 ❭ اوامر الموسيقي للقنوات والجروبات ⇊
🤵╜ « المنشئ » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
▶️╖ تشغيل «» ريبلاي علي اغنيه
🎶╢ تشغيل + اسم الاغنيه
📹╢ فيديو + اسم الفديو
🔴╢ تشغيل + لينك بث مباشر
⏹╢ ايقاف
⏯️╢ تخطي
👷‍♂️╢ الحساب المساعد
🔢╜ قائمه التشغيل
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m6 (\\d+)$"))
async def m6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾", url=f"https://t.me/AWCODE3")],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
💎╖ ❬ م6 ❭ اوامر المطورين ⇊
👮‍♂️╜ « المطور » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
🤴╖ رفع «» تنزيل ❬ مالك ❭
🔂╢ تغيير رابط الجروب
🔊╢ اذاعه بالمجموعات
👨‍🏭╢ اذاعه بالتوجيه للمجموعات
🤹‍♀╢ اذاعه موجهه بالتثبيت
☀️╢ اذاعه خاص
💘╢ اذاعه بالتوجيه خاص
🎙️╢ اذاعه بالتثبيت
📶╢ جلب نسخه احتياطيه
🏋‍♂╢ رفع نسخه احتياطيه
🍃╢ الاحصائيات
🚷╢ حذف المالكين
📚╜ ❬ + ❭ جميع ماسبق
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
💎 « المطور الاساسي » ⇊
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
📑╖ اضف «» حذف رد عام
🤴╢ رفع «» تنزيل ❬ مميز عام ❭
💎╢ مسح المميزين عام
🗃️╢ الردود العامه
🧨╢ حذف الردود العامه
🛠╢ اذاعه بالتوجيه خاص
🍃╢ اذاعه بالتوجيه للمجموعات
🎯╢ اذاعه بالتثبيت
☀️╢ اذاعه موجهه بالتثبيت
🧲╢ جلب «» رفع ❬نسخه احتياطيه❭
⏳╢ الاحصائيات
🤴╢ رفع «» تنزيل ❬ مطور ❭
🤖╢ المطورين «» حذف المطورين
🔗╢ ضع اسم للبوت
📝╢ تغيير رساله المغادره
🚫╢ حظر «» كتم  ❬ عام ❭
🥺╢ المكتومين  عام 
💔╢ المحظورين عام
♻️╢ الغاء العام
📚╜ ❬ + ❭ جميع ماسبق
●━━━‌‌𝑆𝑂𝑈𝑅𝐶𝐸 𝐽𝐴𝐶𝐾━━━●
    """, reply_markup=keyboard)
