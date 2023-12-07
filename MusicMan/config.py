# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQFwDSIAHYGW1QnUX3jZhJC2MJaphnsOqD7AQfZ6a0VxofWFiysxWbqD9CvwMdIMTBwzR0jMiph7JG6dyJ5jWd45ePqpoWvqb6dIWYAz2hM1XSC5PAMS7m3gQJLg8C_6d-BBDsxl_Io8o4XuAfbvNnGizwMVHDRrqwF0k0hkk7-zJ_cd1PavTIAzZ7Ul4Z7FiqT6oYNxwy0RuH9fLgd5mS0j0EoRakEFRtPCd9rLH4YqCx1RH-jfUHCPVaW9rrYr6YspjbhlbUCQRwbX9dswagCTRdDrt22cvJMgYl7VpY_Wn3xPp7hna9AejX7v3cK6ldqSmJXs5B-qvpOngjfrV9k12Qrb0gAAAAGFcEZWAA")
BOT_TOKEN = getenv("BOT_TOKEN", "6803743701:AAErjLVnkun9QasfCjmmRd46GdWx1Zpk8bo")
BOT_NAME = getenv("BOT_NAME", "𝗣𝗔𝗞𝗗𝗛𝗘 𝗠𝗨𝗦𝗜𝗞")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "friendshipstoree")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph//file/78b35165e01a5321c719c.jpg")
admins = {}
API_ID = int(getenv("API_ID", "24120610"))
API_HASH = getenv("API_HASH", "efbf38b7a8ef18796a0ee7028cc67013")
BOT_USERNAME = getenv("BOT_USERNAME", "@Pakdhemusikbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "botmusikman")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "friendshipsuport")
PROJECT_NAME = getenv("PROJECT_NAME", "𝗣𝗔𝗞𝗗𝗛𝗘 𝗠𝗨𝗦𝗜𝗞")
OWNER = getenv("OWNER", "@pakdiih")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/mrismanaziz/Music-Man")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "30"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "-1001794660377")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
