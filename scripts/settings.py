from dotenv import load_dotenv
from pathlib import Path
import os

ROOT_PATH = Path(os.path.dirname(__file__)).parents[0]

# using .env file to grab private token
env_path = Path(ROOT_PATH) / '.env'
load_dotenv(dotenv_path = env_path)

TOKEN = os.getenv("TOKEN")
PREFIX = "yeetus "
