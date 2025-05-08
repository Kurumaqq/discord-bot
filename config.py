from dotenv import load_dotenv
from os import getenv


load_dotenv()

SERVER_ID = getenv('SERVER_ID')
TOKEN = getenv('TOKEN')
ADMIN_ROLE = getenv('ADMIN_ROLE')