from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product


ds_praktikum = Product(
    title="Data Science va Sun'iy intellekt",
    description="Kursga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="uzs",
    prices=[
        LabeledPrice(
            label='Praktikum',
            amount=15000000, #150.000.00 so'm
        ),
        LabeledPrice(
            label='Chegirma',
            amount=-1000000, #-10.000.00 so'm
        ),
        
    ],
    start_parameter="create_invoice_ds_praktikum",
    photo_url='https://d3njjcbhbojbot.cloudfront.net/api/utilities/v1/imageproxy/https://coursera_assets.s3.amazonaws.com/xdp/decisionCriteriaBannerLogos/google-data-analytics.png?auto=format%2Ccompress&dpr=1&w=&h=260',
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
)

python_book = Product(
    title="Pythonda Dasturlash Asoslari",
    description="Kitobga to'lov qilish uchun quyidagi tugmani bosing.",
    currency="uzs",
    prices=[
        LabeledPrice(
            label='Kitob',
            amount=5000000,#50.000.00 so'm
        ),
        LabeledPrice(
            label='Yetkazib berish (7 kun)',
            amount=1000000,#10.000.00 so'm
        ),
    ],
    start_parameter="create_invoice_python_book",
    photo_url='https://i.imgur.com/0IvPPun.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True, # dastofka uchun 
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (3 kun)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 1500000),
        LabeledPrice(
            '3 ish kunida yetkazish', 500000),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 2500000),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -1000000)
                                       ])