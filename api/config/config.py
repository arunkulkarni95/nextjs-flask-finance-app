import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ALPHA_VANTAGE_API_KEY = os.environ.get('ALPHA_VANTAGE_API_KEY')
