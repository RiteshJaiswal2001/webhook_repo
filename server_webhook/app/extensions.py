from flask_pymongo import PyMongo

# Setup MongoDB here 

from dotenv import load_dotenv
import os

load_dotenv()

mongo = PyMongo()
