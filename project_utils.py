import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://d4vm:Da19tka90@cluster0.xbv7wim.mongodb.net/?retryWrites=true&w=majority"


def validate_url(provided_url: str) -> bool:
    """
    Validates URL provided by user request.
    If URL is valid for www.myauto.ge, and has product ID. returns True.

    :param provided_url:
    :return:
    """

    # Regex Patterns
    pattern_digits = r'\d{8}'  # Finding Digits
    pattern_myauto_ge = r'myauto\.ge'  # Finding Text

    check_digits = re.search(pattern_digits, provided_url)
    check_myauto_ge = re.search(pattern_myauto_ge, provided_url)

    return bool(check_digits) and bool(check_myauto_ge)


def extract_url_id(provided_url: str) -> str:
    """
    Extracts ID from myauto.ge URL

    :param provided_url:
    :return:
    """
    pattern_digits = r'\d{8}'  # finding digits
    product_id = re.search(pattern_digits, provided_url)
    return product_id.group(0)


def test_db_connection(uri: str) -> bool:
    """
    Testing if connection to free tier database is successful.
    :return:
    """
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        # print("Pinged Successfully. Connected to MongoDB!")
        connection_status = True
    except Exception:
        connection_status = False

    return connection_status

debug = True