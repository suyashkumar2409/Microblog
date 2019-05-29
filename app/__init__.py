from flask import Flask

app = Flask(__name__)

# app is the current module. It will soon include a routes file
from app import routes
