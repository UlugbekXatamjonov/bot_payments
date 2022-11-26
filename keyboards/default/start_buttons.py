from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(
	keyboard  = [
		[
			KeyboardButton(text="kitob"),
			KeyboardButton(text='praktikum'),
		],
		[
			KeyboardButton(text="mahsulotlar"),
		],

	],
	resize_keyboard=True

)

