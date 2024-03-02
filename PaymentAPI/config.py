from dotenv import load_dotenv
import os

load_dotenv()

STRIPE_API_KEY = os.environ.get('STRIPE_API_KEY')
DJANGO_KEY = os.environ.get('DJANGO_KEY')
