import os

API_ID = API_ID = 22609670

API_HASH = os.environ.get("API_HASH", "3506d8474ad1f4f5e79b7c52a5c3e88d")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6711741427:AAGrYQvfpms_7_wIIvHfnOWzUwkQF_2uKlM")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6981453498))

LOG = -1001847674314

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6981453498").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


