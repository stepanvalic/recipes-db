from flask import Flask, send_from_directory
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, static_folder='.')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')

from app import routes, models