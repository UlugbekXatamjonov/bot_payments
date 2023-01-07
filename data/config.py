# from environs import Env
from environs import Env

# env = Env()
# env.read_env()

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
PROVIDER_TOKEN = env.str("PROVIDER_TOKEN","PROVIDER_TOKEN_GP")


import os

# .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))  # Bot token
# ADMINS = str(os.environ.get("ADMINS"))  # adminlar ro'yxati
# IP = str(os.environ.get("ip"))  # Xosting ip manzili
# PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))


# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN='5855682744:AAE3TpgV7tB3N6UJ36HqU3WAQo-subQQmD8'
# ADMINS =1012480055 
# # IP = 
# PROVIDER_TOKEN =371317599:TEST:1673054897897
