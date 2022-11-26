# from environs import Env

# env = Env()
# env.read_env()

# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
# PROVIDER_TOKEN = env.str("PROVIDER_TOKEN","PROVIDER_TOKEN_GP")


import os

# .env fayli ichidan quyidagilarni o'qiymiz
BOT_TOKEN = str(os.environ.get(("BOT_TOKEN")))
ADMINS = str(os.environ.get(("ADMINS")))
IP = str(os.environ.get(("ip")))
PROVIDER_TOKEN = str(os.environ.get(("PROVIDER_TOKEN")))



