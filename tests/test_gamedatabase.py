import os

import pandas
import pytest
from dotenv import load_dotenv
from pymongo import MongoClient

import gamedatabase
from users import ActiveUser

load_dotenv()

DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

test_database = None
test_collection = None




def test_insert_document():
    assert False
def test_modify_value():
    assert False

def test_get_document():
    assert False

def test_delete_document():
    assert False
