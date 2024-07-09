
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
import logging
load_dotenv()
logging.getLogger('flask_cors').level = logging.DEBUG
app = Flask(__name__)
CORS(app)


