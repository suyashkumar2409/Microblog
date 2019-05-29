from flask import Flask

app = Flask(__name__)

# app is the current module. It will soon include a routes file
# it needs to be declared after making app because routes uses app variable
# initialised here. Had it been called before, routes would have run
# and it wouldn't have know which variable app is
from app import routes
