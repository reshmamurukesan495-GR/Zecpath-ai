import os
from dotenv import load_dotenv
load_dotenv()
APP_NAME = "Zecpath AI"
ENVIRONMENT = os.getenv("ENVIRONMENT","development")