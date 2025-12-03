print('Practice environment variable')

from dotenv import load_dotenv
import os

load_dotenv('.env')

username: str = os.getenv('USER_NAME')

print(username)