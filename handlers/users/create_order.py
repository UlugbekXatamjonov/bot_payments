from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS

from loader import dp, bot
from data.products import python_book, ds_praktikum,  FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING
from keyboards.inline.product_keys import build_keyboard


@dp.message_handler(text="kitob")
async def show_invoices(message: types.Message):
    caption = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n\n"
    caption += "Ushbu kitob bugungi kunda dasturlash asoslariga oid o’zbek tilidagi mukammal tuzilgan qo’llanmalardan biridir.\n\n"
    caption += "Qo’lingizdagi kitobning o’ziga xos jihati shundaki, uning har bir bo’limi uchun tayyorlangan qo'shimcha onlayn"
    caption += "materiallar, jumladan, 50 dan ortiq video darslar, amaliy mashg’ulotlar va vazifalarning kodlari e’tiboringizga havola etilgan.\n\n"
    caption += "O’quvchilar bu materiallarni maxsus QR kod yordamida o’z komputerlariga yuklab olib, ulardan unumli foydalanishi mumkin.\n\n"
    caption += "Narxi: <b>50000 so'm</b>"
    await message.answer_photo(photo="https://i.imgur.com/0IvPPun.jpg",
                         caption=caption, reply_markup=build_keyboard("book"))

@dp.message_handler(text="praktikum")
async def show_invoices(message: types.Message):
    caption = "<b>Google Data Analytics Professional Certificate</b>\n\n"
    caption += "This is your path to a career in data analytics. In this program\n\n"
    caption += "✅ You’ll learn in-demand skills that will have you job-ready in less than 6 months\n"
    caption += "✅ No degree or experience required\n"
    caption += "✅ Build job-ready skills by learning from the best\n"
    caption += "Prise: <b>1.5mln so'm(150$)</b>"

    await message.answer_photo(photo="https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera_assets.s3.amazonaws.com/xdp/decisionCriteriaBannerLogos/google-data-analytics.png?auto=format%2Ccompress&dpr=1&w=&h=260",
                         caption=caption, reply_markup=build_keyboard("praktikum"))




@dp.message_handler(text="mahsulotlar")
async def book_invoice(message: Message):
    await bot.send_invoice(chat_id=message.from_user.id,
                           **python_book.generate_invoice(),
                           payload="123456")
    await bot.send_invoice(chat_id=message.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="123457")


@dp.callback_query_handler(text="product:book")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **python_book.generate_invoice(),
                           payload="payload:kitob")
    await call.answer()


@dp.callback_query_handler(text="product:praktikum")
async def praktikum_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **ds_praktikum.generate_invoice(),
                           payload="payload:praktikum")
    await call.answer()



@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "namangan": 
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")
