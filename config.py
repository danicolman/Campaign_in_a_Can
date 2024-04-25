import os
from dotenv import dotenv_values

basedir = os.path.abspath(os.path.dirname(__file__))

dnd = {"url": "https://www.dnd5eapi.co", "headers": {"Accept": "application/json"}}

config = dict(dotenv_values(".env"))
