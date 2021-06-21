import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CSK = os.environ.get("consumer_key")
CSS = os.environ.get("consumer_secret")
AST = os.environ.get("access_token")
ATS = os.environ.get("access_token_secret")
