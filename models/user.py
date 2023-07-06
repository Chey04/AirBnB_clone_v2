#!/usr/bin/python3
"""User is a subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''subclass of BaseModel class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
